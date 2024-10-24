"""
Student information for this assignment:

Replace <FULL NAME> with your name.
On my/our honor, <KAVYA CHOWTI> and <ETHAN MIKEL>, this
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
    """
    Initializes the linked list head
    """
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
        """
        Inserts the term with the coefficient coeff and exponent exp into the polynomial.
        If a term with that exponent already exists, we add the coefficients together.
        It also keeps the terms in descending order by exponent.
        """
        if coeff == 0:
            return

        new_node = Node(coeff, exp)

        if self.head is None or exp > self.head.exp:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            previous = None
            while current and current.exp > exp:
                previous = current
                current = current.next

            if current and current.exp == exp:
                current.coeff += coeff
                if current.coeff == 0:
                    if previous:
                        previous.next = current.next
                    else:
                        self.head = current.next
            else:
                new_node.next = current
                if previous:
                    previous.next = new_node
                else:
                    self.head = new_node


    # Add a polynomial p to the polynomial and return the resulting polynomial as a new linked list.
    def add(self, p):
        """
        Adds a polynomial p to the polynomial and returns 
        the resulting polynomial as a new linked list.
        """
        result = LinkedList()
        node1 = self.head
        node2 = p.head

        while node1 is not None or node2 is not None:
            if node1 is not None and node2 is not None:
                if node1.exp > node2.exp:
                    result.insert_term(node1.coeff, node1.exp)
                    node1 = node1.next
                elif node2.exp > node1.exp:
                    result.insert_term(node2.coeff, node2.exp)
                    node2 = node2.next
                else:
                    sum_coeff = node1.coeff + node2.coeff
                    if sum_coeff != 0:
                        result.insert_term(sum_coeff, node1.exp)
                    node1 = node1.next
                    node2 = node2.next
            elif node1 is not None:
                result.insert_term(node1.coeff, node1.exp)
                node1 = node1.next
            elif node2 is not None:
                result.insert_term(node2.coeff, node2.exp)
                node2 = node2.next

        return result


    # Multiply a polynomial p with the polynomial and return the product as a new linked list.
    def mult(self, p):
        """
        Multiply a polynomial p with the polynomial and return the product as a new linked list.
        """
        result = LinkedList()
        node1 = self.head

        while node1:
            node2 = p.head
            while node2:
                result.insert_term(node1.coeff * node2.coeff, node1.exp + node2.exp)
                node2 = node2.next
            node1 = node1.next

        return result

    # Return a string representation of the polynomial.
    def __str__(self):
        """
        Return a string representation of the polynomial.
        """
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
    """
    Reads the data froma file and creates two polynomials
    p and q. Returns the sum and product of p and q
    using a linked list.
    """
    n = int(input())
    p = LinkedList()
    for _ in range(n):
        coeff, exp = map(int, input().split())
        p.insert_term(coeff, exp)

    input()

    m = int(input())
    q = LinkedList()
    for _ in range(m):
        coeff, exp = map(int, input().split())
        q.insert_term(coeff, exp)

    sum_poly = p.add(q)
    product_poly = p.mult(q)

    print(sum_poly)
    print(product_poly)

if __name__ == "__main__":
    main()