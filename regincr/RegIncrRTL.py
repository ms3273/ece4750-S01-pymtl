#=======================================================================
# RegIncrRTL.py
#=======================================================================
# RTL model of a registered incrementer.

from pymtl import *

class RegIncrRTL( Model ):

  def __init__( s, dtype ):
    s.in_ = InPort ( dtype )
    s.out = OutPort( dtype )

    #-------------------------------------------------------------------
    # TASK 2.3: Comment out the Exception below.
    #           Implement RegIncr code shown on the overhead slides.
    #-------------------------------------------------------------------

    raise NotImplementedError(
      'RegIncrRTL has not been implemented yet!\n '
      'Put your implementation code here!'
    )


  def line_trace( s ):
    return '{} ({}) {}'.format( s.in_, s.tmp, s.out )
