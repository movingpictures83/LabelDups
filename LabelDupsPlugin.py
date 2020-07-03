class LabelDupsPlugin:
   def input(self, filename):
      f = open(filename, 'r')
      self.taxa = f.readline().strip().split(',') # Taxa are on the first line
      self.contents = []
      for line in f:
         self.contents.append(line)


   def run(self):
      self.labeledtaxa = []
      counts = dict()
      for taxon in self.taxa:
         if (taxon not in self.labeledtaxa):
            self.labeledtaxa.append(taxon)
         else:
            if (taxon not in counts): 
               counts[taxon] = 1
            else:
               counts[taxon] += 1
            if (taxon[0] == '\"'):
               labeledtaxon = '\"' + taxon[1:len(taxon)-1] + "-" + str(counts[taxon]) + '\"'
            else:
               labeledtaxon = taxon+"-"+str(counts[taxon])
            self.labeledtaxa.append(labeledtaxon)

   def output(self, filename):
      g = open(filename, 'w')
      # Write first line again
      for i in range(len(self.labeledtaxa)):
         g.write(self.labeledtaxa[i])
         if (i != len(self.labeledtaxa)-1):
            g.write(',')
         else:
            g.write('\n')
      for line in self.contents:
         g.write(line)
