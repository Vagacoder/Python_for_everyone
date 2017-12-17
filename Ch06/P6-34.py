import numpy
import scipy.io.wavfile

def main() :
    inputName = input("Input file: ")

    contents = scipy.io.wavfile.read(inputName)
    sampleRate = contents[0]
    data = contents[1].tolist()


    outputdata = process(data, sampleRate)
    outputName = inputName.replace(".wav", ".out.wav")
    scipy.io.wavfile.write(outputName, sampleRate,
      numpy.asarray(outputdata, dtype="int16"))

def process(data, sampleRate) :
    result = []

    for i in range(len(data)) :
        if (i >= 0.2* sampleRate) :
            data[i] = data[i] + data[i - int(0.2* sampleRate)]
            result.append(data[i])

    maxA = max(result)
    rate = 32767/maxA

    result1 = []
    for i in result:
        result1.append(i*rate)


    return result

    
# Start the program.
main()
