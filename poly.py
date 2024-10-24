"""
Student information for this assignment:

Replace <FULL NAME> with your name.
On my/our honor, Kavya Chowti and Ethan Mikel, this
programming assignment is my own work and I have not provided this code to
any other student.

I have read and understand the course syllabus's guidelines regarding Academic
Integrity. I understand that if I violate the Academic Integrity policy (e.g.
copy code from someone else, have the code generated by an LLM, or give my
code to someone else), the case shall be submitted to the Office of the Dean of
Students. Academic penalties up to and including an F in the course are likely.

UT EID 1: kc45736
UT EID 2: etm693
"""

class Node:
    """
    A modified version of the Node class for linked lists (using proper class
    coding practices). Instead of a data instance variable, this node class has both
    a coefficient and an exponent instance variable, which is used to represent each
    term in a polynomial.
    """

    def __init__(self, coeff, exp, link=None):
        """
        Node Constructor for polynomial linked lists.

        Args:
        - coeff: The coefficient of the term.
        - exp: The exponent of the term.
        - link: The next node in the linked list.
        """
        self.coeff = coeff
        self.exp = exp
        self.next = link

    @property
    def coeff(self):
        """
        Getter method for the coefficient attribute.
        """
        return self.__coeff

    @coeff.setter
    def coeff(self, value):
        """
        Setter method for the coefficient attribute.
        """
        if value is None or isinstance(value, int):
            self.__coeff = value
        else:
            raise ValueError("Coefficient must be an integer or None.")

    @property
    def exp(self):
        """
        Getter method for the exponent attribute.
        """
        return self.__exp

    @exp.setter
    def exp(self, value):
        """
        Setter method for the exponent attribute.
        """
        if value is None or isinstance(value, int):
            self.__exp = value
        else:
            raise ValueError("Exponent must be an integer or None.")

    @property
    def next(self):
        """
        Getter method for the next attribute.
        """
        return self.__next

    @next.setter
    def next(self, value):
        """
        Setter method for the next attribute.
        """
        if value is None or isinstance(value, Node):
            self.__next = value
        else:
            raise ValueError("Next must be a Node instance or None.")

    def __str__(self):
        """
        String representation of each term in a polynomial linked list.
        """
        return f"({self.coeff}, {self.exp})"


class LinkedList:
    def __init__(self):
        # You are also welcome to use a sentinel/dummy node!
        # It is definitely recommended, which will we learn more
        # about in class on Monday 10/21. If you choose to use
        # a dummy node, you can comment out the self.head = None
        # and comment in the below line. We use None to make sure
        # if there is an error where you accidentally include the
        # dummy node in your calculation, it will throw an error.
        # self.dummy = Node(None, None)
        self.head = None

    # Insert the term with the coefficient coeff and exponent exp into the polynomial.
    # If a term with that exponent already exists, add the coefficients together.
    # You must keep the terms in descending order by exponent.
    def insert_term(self, coeff, exp):
       if coeff == 0:
            return
        
        new_node = Node(coeff, exp)

        if self.head is None or exp > self.head.exp:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.exp > exp:
                current = current.next

            if current.exp == exp:
                current.coeff += coeff
                if current.coeff == 0:
                    self._delete_node(current)
            else:
                new_node.next = current.next
                current.next = new_node

    # Add a polynomial p to the polynomial and return the resulting polynomial as a new linked list.
    def add(self, p):
        result = LinkedList()
        p1, p2 = self.head, p.head

        while p1 or p2:
            if p1 and (not p2 or p1.exp > p2.exp):
                result.insert_term(p1.coeff, p1.exp)
                p1 = p1.next
            elif p2 and (not p1 or p2.exp > p1.exp):
                result.insert_term(p2.coeff, p2.exp)
                p2 = p2.next
            else:
                result.insert_term(p1.coeff + p2.coeff, p1.exp)
                p1, p2 = p1.next, p2.next

        return result

    # Multiply a polynomial p with the polynomial and return the product as a new linked list.
    def mult(self, p):
        result = LinkedList()
        p1 = self.head

        while p1:
            temp = LinkedList()
            p2 = p.head

            while p2:
                temp.insert_term(p1.coeff * p2.coeff, p1.exp + p2.exp)
                p2 = p2.next
            
            result = result.add(temp)
            p1 = p1.next
        
        return result

    # Return a string representation of the polynomial.
    def __str__(self):
        if not self.head:
            return ""

        terms = []
        current = self.head
        while current:
            coeff = current.coeff
            exp = current.exp

            if coeff == 0:
                current = current.next
                continue
            
            terms.append(f"({coeff}, {exp})")

            current = current.next

        return " + ".join(terms)



def main():
    poly1 = LinkedList()
    num_terms1 = int(input("Enter the number of terms for the first polynomial: "))
    for _ in range(num_terms1):
        data = input("Enter terms for the first polynomial (coeff exp). Type 'end' to stop: ")
        if data.strip().lower() == 'end':
            break
        try:
            coeff, exp = map(int, data.split())
            poly1.insert_term(coeff, exp)
        except ValueError:
            print("Invalid input. Please enter two integers separated by a space.")
            continue

    poly2 = LinkedList()
    num_terms2 = int(input("Enter the number of terms for the second polynomial: "))
    for _ in range(num_terms2):
        data = input("Enter terms for the second polynomial (coeff exp). Type 'end' to stop: ")
        if data.strip().lower() == 'end':
            break
        try:
            coeff, exp = map(int, data.split())
            poly2.insert_term(coeff, exp)
        except ValueError:
            print("Invalid input. Please enter two integers separated by a space.")
            continue

    result_add = poly1.add(poly2)
    result_mult = poly1.mult(poly2)

if __name__ == "__main__":
    main()
