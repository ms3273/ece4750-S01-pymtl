#=========================================================================
# GCD Unit FL Model
#=========================================================================

from fractions  import gcd

from pymtl      import *
from pclib.ifcs import InValRdyBundle, OutValRdyBundle, valrdy_to_str
from pclib.fl   import InValRdyQueueAdapter, OutValRdyQueueAdapter

from GcdUnitMsg import GcdUnitReqMsg

class GcdUnitFL( Model ):

  # Constructor

  def __init__( s ):

    # Interface

    s.req    = InValRdyBundle  ( GcdUnitReqMsg() )
    s.resp   = OutValRdyBundle ( Bits(16)        )

    # Adapters

    s.req_q  = InValRdyQueueAdapter  ( s.req  )
    s.resp_q = OutValRdyQueueAdapter ( s.resp )

    # Concurrent block

    @s.tick_fl
    def block():

      #-------------------------------------------------------------------
      # TASK 3.2: Comment out the Exception below.
      #           Implement GcdUnitFL code shown on the slides.
      #-------------------------------------------------------------------

      raise NotImplementedError(
        'GcdUnitMsg has not been implemented yet!\n '
        'Put your implementation code here!'
      )

  # Line tracing

  def line_trace( s ):
    return "{}(){}".format( s.req, s.resp )

