def add_extra_security(func):


    def wrapper():
        print("1.Before the function is called.")
        print("2.Add Helmet, Dashcam, Gloves, Knee Guard, License")
        func()    # drive_Ola_scooter and driving_scooty
        print("3. After the function is called")
        print("4.Secure Driving ,Leave all the items")

    return wrapper()

@add_extra_security
def drive_Ola_scooter():
    print("Drive OLA")


@add_extra_security
def driving_scooty():
    print("Normal Function!!")
    print("I am driving a scooty")