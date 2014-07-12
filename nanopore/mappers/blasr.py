from nanopore.mappers.abstractMapper import AbstractMapper
from sonLib.bioio import system
import os

class Blasr(AbstractMapper):
    def run(self):
        system("blasr %s %s -sam > %s" % (self.readFastqFile, self.referenceFastaFile, self.outputSamFile))

class BlasrChain(Blasr):
    def run(self):
        Blasr.run(self)
        self.chainSamFile()

class BlasrRealign(Blasr):
    def run(self):
        Blasr.run(self)
        self.realignSamFile()
