#!/usr/bin/env python3

import sys
import subprocess

class EncryptionDriver:
    
    # communication for logger + encryptor
    def __init__(self, logfile_txt):
        self.logfile_txt = logfile_txt
        self.history = []
        self.logger = None
        self.encryptor = None
    
    # start logger + encryptor
    def start(self):
        self.logger = subprocess.Popen(
            [sys.executable, "logger.py", self.logfile_txt],
            stdin = subprocess.PIPE,
            text = True
        )
        self.encryptor = subprocess.Popen(
            [sys.executable, "encryption.py"],
            stdin = subprocess.PIPE,
            stdout = subprocess.PIPE,
            text = True
        )
        self.log("START", "Driver started")
    
    # send log to logger
    def log(self, action, message=""):
        self.logger.stdin.write(f"{action} {message}\n")
        self.logger.stdin.flush()
    
    # send command to encryptor w/ responce
    def send_to_encryptor(self, command, argument=""):
        message = f"{command} {argument}\n" if argument else f"{command}\n"
        self.encryptor.stdin.write(message)
        self.encryptor.stdin.flush()
        response = self.encryptor.stdout.readline()
        return response.rstrip()
    
    # retrieve user input
    def get_user_input(self, prompt, use_history=True):
        use_hist = False
        if use_history:
            answer = input("Use history? (y/n) ").strip().lower()
            if answer == "y":
                use_hist = True

        if use_hist:
            selected = self.select_from_history()
            if selected:
                return selected
            
        return self.get_valid_letters(prompt)
    
    # user select from history
    def select_from_history(self):
        if not self.history:
            print("  (history is empty)")
            return None
        
        # history with index displayed
        for i in range(len(self.history)):
            print(f"  {i + 1}: {self.history[i]}")
        print("  0: enter new")
        
        selection = input("Select number: ").strip()
        if selection.isdigit():
            index = int(selection)
            if index == 0:
                return None

            # if index valid, return item
            if 1 <= index <= len(self.history):
                return self.history[index - 1]
        return None
    
    # only valid letters
    def get_valid_letters(self, prompt):
        valid = False
        while not valid:
            user_text = input(prompt).strip()
            if user_text.isalpha():
                valid = True
            else:
                print("Invalid input. Only letters A-Z allowed.")
        return user_text.upper()
            
    def handle_password(self):
        user_password = self.get_user_input("Enter new password: ")

        result = self.send_to_encryptor("PASS", user_password)
        print(result)

        self.log("ENC", f"PASS {user_password}")
        self.log("ENCRES", result)
    
    def handle_encrypt(self):
        plain_text = self.get_user_input("Enter text to encrypt: ")
        
        if plain_text not in self.history:
            self.history.append(plain_text)
        
        response = self.send_to_encryptor("ENCRYPT", plain_text)
        print(response)
        
        if response.startswith("RESULT "):
            cipher = response.split(None, 1)[1]
            self.history.append(cipher)
        
        self.log("ENC", f"ENCRYPT {plain_text}")
        self.log("ENCRES", response)
    
    def handle_decrypt(self):
        encrypted_text = self.get_user_input("Enter text to decrypt: ")
        
        if encrypted_text not in self.history:
            self.history.append(encrypted_text)
        
        response = self.send_to_encryptor("DECRYPT", encrypted_text)
        print(response)
        
        if response.startswith("RESULT "):
            plain = response.split(None, 1)[1]
            self.history.append(plain)
        
        self.log("ENC", f"DECRYPT {encrypted_text}")
        self.log("ENCRES", response)
    
    def show_history(self):
        print("\nHistory:")
        count = 1
        for item in self.history:
            print(f"  {count}: {item}")
            count += 1
    
    def quit(self):
        self.log("EXIT", "Driver exiting")
        self.send_to_encryptor("QUIT")
        self.logger.stdin.write("QUIT\n")
        self.logger.stdin.flush()
        self.encryptor.wait()
        self.logger.wait()
    
    def cleanup(self):
        self.logger.stdin.write("QUIT\n")
        self.logger.stdin.flush()
        self.encryptor.terminate()
        self.logger.terminate()
    
    def run(self):
        commands = {
            "password": self.handle_password,
            "encrypt": self.handle_encrypt,
            "decrypt": self.handle_decrypt,
            "history": self.show_history,
            "quit": self.quit
        }
        
        try:
            while True:
                print("\nCommands: password, encrypt, decrypt, history, quit")
                
                user_command = input("Enter command: ").strip().lower()
                self.log("CMD", user_command)
                
                if user_command == "quit":
                    self.quit()
                    break
                elif user_command in commands:
                    commands[user_command]()
                else:
                    print("Unknown command.")
        
        except KeyboardInterrupt:
            print("\nInterrupted, exiting.")
            self.cleanup()


def main():
    if len(sys.argv) != 2:
        print("Usage: driver.py <logfile>")
        sys.exit(1)
    
    logfile = sys.argv[1]
    driver = EncryptionDriver(logfile)
    driver.start()
    driver.run()


if __name__ == "__main__":
    main()
