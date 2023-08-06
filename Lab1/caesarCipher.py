def main():
    #function to encrypt the given plain text
    def  encryption():
        userInput=input("Enter a text:")
        key = int(input("Enter the key: "))
        print("\n***************************************")
        cipher =[]
        for i in range (len(userInput)):
            unitUserInput=userInput[i]
            if unitUserInput.isupper():
                cipher_char= chr((ord(unitUserInput)-65 +key % 26)+65)
            elif unitUserInput.islower():
                cipher_char= chr((ord(unitUserInput)-97 +key % 26)+97)
            else:
                cipher_char=unitUserInput
            cipher.append(cipher_char)
        for i in range (len(cipher)):
            print(cipher[i],end='')  
    #function to decrypt the given plain text        
    def decryption():
        userInput=input("Enter a text:")
        key = int(input("Enter the key: "))
        print("\n***************************************")
        cipher =[]
        for i in range (len(userInput)):
            unitUserInput=userInput[i]
            if unitUserInput.isupper():
                cipher_char= chr((ord(unitUserInput)-65 -key % 26)+65)
            elif unitUserInput.islower():
                cipher_char= chr((ord(unitUserInput)-97 -key % 26)+97)
            else:
                cipher_char=unitUserInput
            cipher.append(cipher_char)
        for i in range (len(cipher)):
            print(cipher[i],end='')
            
    while True:
        print("\n***************************************")
        print("1. Encryption\n2. Decryption\n3. Exit")
        print("***************************************")
        choice =int(input("Enter your choice:"))
        match choice:
          case 1:
               encryption()
          case 2:
               decryption()
          case 3:
               exit()  
main()  







      