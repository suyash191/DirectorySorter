import os   #Operating System
import shutil   #shell utilities
import sys  #System



def sortDirectory(directory, func=shutil.copy):

    if not os.path.isdir(directory):
        return (1)

    #root = current directory
    #dirs = list of directories in root
    #files = list of files in root
    for root, dirs, files in os.walk(directory):

        #iterating through each file in the files list
        for file in files:

            #name to store file name
            #ext to store file extension
            name, ext = os.path.splitext(file)
            ext = ext[1:]   #store the extension name after skipping the dot(.)

            #to check if the directory where we're moving(or copying) files to, exists
            #os.path.join : joins parameters using correct directory separator (Usually '\')
            if not os.path.exists(os.path.join("out", ext)): #here os.path.join returns "out\ext"
                os.makedirs(os.path.join("out", ext))   #executed if the output folder does not exist

            #check if the file we're moving to the folder exists there or not. If it does, then increase count by 1
            if os.path.exists(os.path.join("out", ext, file)):
                count=1

                for newFile in os.listdir(os.path.join("out", ext, '')):
                    if name == "_".join(newFile.split('.')[0].split('_')[:-1]):
                        count+=1

                outfile = name+'_'+str(count)+'.'+ext   #name of format of 'name_n' where n is the no. of times that file appears
            else:
                outfile = name

            print('File:', os.path.join(root, file), '->', os.path.join("out", ext, outfile))
            func(os.path.join(root, file), os.path.join("out", ext, outfile))

    return 0


def main():

    functionDict={
        'm': shutil.move,
        'c': shutil.copy,
    }
    flag = shutil.copy
    if len(sys.argv) == 3:  #means user gave directory and function (copy or move)

        if sys.argv[2].lower()[0] in functionDict:
            flag = functionDict[sys.argv[2].lower()[0]]
        else:
            print("Unsupported 3rd argument. Use 'm'ove or 'c'opy")
            return 1

    elif len(sys.argv) == 1 or len(sys.argv) > 3:
        print("Wrong amount of arguments. Only 2 arguments supported: [path function]")
        return 1

    return sortDirectory(sys.argv[1], flag)


if __name__ == '__main__':
    main()
