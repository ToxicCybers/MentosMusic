from os import listdir
from os import mkdir

if 'raw_files' not in listdir():
    mkdir('raw_files')

from Music.MusicUtilities.tgcallsrun.convert import convert

__all__ = ['convert']
