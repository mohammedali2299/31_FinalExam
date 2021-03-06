"""
Final exam, problem 4.

Authors: David Mutchler, Dave Fisher, Matt Boutell, Amanda Stouder,
         their colleagues and mohammed ali.  May 2018.

"""  # done: 1. PUT YOUR NAME IN THE ABOVE LINE.


###############################################################################
# done: 2.
#   In this problem, you will go through the methods of the  Pig  class
#   that is defined below, one by one, in the order that they appear.
#   For each method:
#      (a) Read the method's doc-string (i.e., specification in double-quotes).
#            If you do not understand WHAT the method is to do,
#            ask your instructor to clarify it.
#      (b) Implement the method.
#      (c) Write at least SOME code  in  main  that tests your code.
#
###############################################################################

def main():
    """ Tests the  Pig  class. """
    # -------------------------------------------------------------------------
    # WRITE CODE HERE AS NEEDED to TEST the code that you write
    #   in the  Pig  class.  At the least, you must:
    #     -- Construct two Pig objects
    #     -- Call each method that you implement below.
    # -------------------------------------------------------------------------
    pig1 = Pig(5)
    pig2 = Pig(10)
    pig1.get_weight()
    pig2.eat_for_a_year()

class Pig(object):
    def __init__(self, weight):
        """
        What comes in:  The Pig's weight (in pounds).
        Side effects: Sets instance variables as needed by the other methods.
        """
        # done: Implement and test this method.
        self.weight = weight
        self.food = 0

    def get_weight(self):
        """ Returns this Pig's weight. """
        # done: Implement and test this method.
        return self.weight

    def eat(self, pounds_of_slop):
        """
        Increments this Pig's weight by the given pounds_of_slop.
        """
        # done: Implement and test this method.
        self.weight = self.weight + pounds_of_slop
        self.food = self.food + 1
    def eat_for_a_year(self):
        """
        Calls the   eat   method as many times as needed to make this Pig:
          -- eat 1 pound of slop, then
          -- eat 2 pounds of slop, then
          -- eat 3 pounds of slop, the
          -- eat ... [4 pounds, then 5, then 6, then ... ]
          -- eat 364 pounds of slop, then
          -- eat 365 pounds of slop.
        """
        # done: Implement and test this method.
        for k in range(365):
            self.eat(k+1)

    def heavier_pig(self, other_pig):
        """
        Returns either this Pig object or the other given Pig object,
        whichever is heavier.
        """
        # done: Implement and test this method.
        if self.weight > other_pig.weight:
            return self
        else:
            return other_pig
    def new_pig(self, other_pig):
        """
        Returns a new Pig whose weight is the weight of the heavier
          of this Pig and the other_Pig.
        """
        # done: Implement and test this method.
        new_pig = Pig()
        new_pig.weight = self.weight + other_pig.weight

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
