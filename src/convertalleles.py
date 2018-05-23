input_file = str(raw_input('Enter File Name: '))
new_file = str(raw_input('Enter New File Name: '))


try:
        first_file = open(input_file, 'r')              #read from file
        header = next(first_file)                       #save header to write to file later
        outfile = open(new_file, 'w+')                  #open output file
        outfile.write(header)                           #write the header to the output file so we don't have to do this during the loop

except:                                                 #basic exception message if the input file is not found
        print('File not found: ', input_file)
        quit()

for row in first_file:
        newline = ''                                    #use to build the final lines that we will print to the output file later
        row = row.rstrip().split()                      #since input file is tab delimmited, remove tabs and spaces
        newline += '{0}\t{1}\t{2}\t{3}'.format(row[0], row[1], row[2], row[3])                  #construct a new line which consists of row[0] (chrom), row[1] (pos), row[2] (ref allele), row[3] (alternate allele), separated by tabs
        allele = row[2]                                 #char allele we are referencing against
        for i in range(4, len(row)-1):                  #already used VariantsToTable script to reduce to the format chrom, pos, ref, alt, and then subject rows (this works for any number of subjects)
                check = row[i].split('/')               #split each allele by '/' to get the chars alone
                new = ''                                #new empty array to hold the corrected allele
                for j in check:
                        if j == '*':                    #if the allele is represented as a *, then replace as a * because we don't want false reads for alleles on individuals
                                new += '*'
                        elif j == '.':                  #if the allele is represented as a ., then replace as a . because we don't want false reads for alleles on individuals
                                new += '.'
                        elif j != allele:               #if the allele is different than the reference allele, then replace with a 1 to show deviation, will result in 1/0, 0/1, or 1/1 final allele
                                new += '1'
                        else:
                                new += '0'              #if the allele is the same as the reference allele, then replace with a 0 to show there is not deviation, results in 0/0, 0/1, or 1/0 final allele
                        new += '/'                      #append a / after each number so the final allele will look something like: 0/0/, 0/1/, 1/1/
                newline += '\t' + new[:-1]              #add a tab after the allele, but delete the trailing /, so the final allele will look like 0/0, 0/1, 1/1
        outfile.write(newline + '\n')                   #write the lines to the output file and append a new line character at the end of each line

