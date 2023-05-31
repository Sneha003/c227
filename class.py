print("welcome to the world of cryptography")

def main():
    print()
    print("choose one option below")
    choice=int(input("1.Encryption\n2.Decription\nchoose(1,2):"))
    if choice ==1:
        encryption()
    elif choice ==2:
        decryption()
    else:
        print("wrong choice")

def encryption():
    print("encription started..")
    print()

    message=input("enter your message: ")
    key=int(input("enter the key(1-94): "))

    encrypted_text=""

    for i in range(len(message)):
        temp=(ord(message[i])+key)
        print(temp)
        if(temp>127):
            temp=temp-127+32
            print(temp)

        encrypted_text+=chr(temp)

    print("encrypted",encrypted_text)
    


def decryption():
    print("decryption started..")
    print()
    print("message can only be lower or uppercase")

    ensc_msg= input("enter the encrypted text: ")
    decr_key=int(input("enter the key(1-94): "))

    decrypted_text=""

    for i in range(len(ensc_msg)):
        temp=(ord(ensc_msg[i])-decr_key)
        print(temp)
        if temp<32:
            temp=temp+127-32

        decrypted_text+=chr(temp)

    print("decrepted text: ",decrypted_text)


    

if __name__=="__main__":
    main()