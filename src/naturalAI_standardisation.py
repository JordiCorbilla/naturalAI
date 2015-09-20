## naturalAI framework
## Copyright (c) 2015, Jordi Corbilla
## All rights reserved.
##
## Redistribution and use in source and binary forms, with or without
## modification, are permitted provided that the following conditions are met:
##
## - Redistributions of source code must retain the above copyright notice,
## this list of conditions and the following disclaimer.
## - Redistributions in binary form must reproduce the above copyright notice,
## this list of conditions and the following disclaimer in the documentation
## and/or other materials provided with the distribution.
## - Neither the name of this library nor the names of its contributors may be
## used to endorse or promote products derived from this software without
## specific prior written permission.
##
## THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
## AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
## IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
## ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
## LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
## CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
## SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
## INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
## CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
## ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
## POSSIBILITY OF SUCH DAMAGE.

class Standardizer:
    def __init__(self, filename):
        # load files from a CSV comma separated values file
        
        values = list(map(lambda l: [int(x) for x in (l.strip()).split(",")],
                     (open(filename, 'r').readlines())   ))

        print ("File Content:")
        for l in values:
            print (l)
        
        # Normalization: substract mean and divide by std deviation
        import numpy
        
        values = numpy.array(values, dtype=float)

        #Array transformation
        print ("Array transformation:")
        for l in values:
            print (l)

        #We need to do the average of the entire column, that's why axis=0
        prom = numpy.average(values, axis=0)
        print ("Average:")
        print (prom)    
        stds = numpy.std(values, axis=0)
        print ("Standard Deviation:")
        print (stds)      

        #Recalculate the content of the properties
        for l in values:
            for i in range(0,len(l)-2):
                l[i]= (l[i] - prom[i]) / stds[i]

        
        valuesNoLastColums = numpy.delete(values, -1, 1)
        valuesNoLastColums = numpy.delete(valuesNoLastColums, -1, 1)    
        self.values = values
        self.valuesNoLastColumns = valuesNoLastColums

    def getValues(self):
        return self.values, self.valuesNoLastColumns   
