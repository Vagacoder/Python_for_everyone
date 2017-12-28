done = False
while not done:
    try:

        filename = input('Please enter file name: ')
        data = open(filename, 'r')
        line = int(data.readline())
        print(line)
        done = True

    except IOError:
        print("Error: file not found.")
    except ValueError:
        print("Error: file contents invalid.")
    except RuntimeError as error:
        print("Error:", str(error))
