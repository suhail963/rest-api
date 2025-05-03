Adaption of Pollard’s kangaroo algorithm to the
FACTOR problem
Mario Romsy
Fakultät für Informatik
Universität der Bundeswehr München
mario.romsy@unibw.de
Abstract
In[BKT11]Baba,KotyadaandTejaintroducedtheFACTORproblem
over non-abelian groups as base of an ElGamal-like cryptosystem. They
conjectured that there is no better method than the naive one to solve
the FACTOR problem in a general group. Shortly afterwards Stanek
published an extension of the baby-step giant-step algorithm disproving
this conjecture [Sta11]. Since baby-step giant-step methods are limited
in practice because of memory requirements we present a modification of
Pollard’skangarooalgorithmthatsolvestheFACTORproblemrequiring
only negligible memory.
1 Introduction
Let n ≥ 2 and (G,·) be a non-abelian finite group with identity element e.
Suppose g ,...,g ∈G with (cid:104)g ,...,g (cid:105)∩(cid:104)g (cid:105)={e} for all i≤n−1 and let
1 n 1 i i+1
x ,...,x ∈Z. Given an element
1 n
h=gx1 ·...·gxn
1 n
we wish to determine g
x1,...,g
xn (we note that the conditions on g
,...,g
imply the uniqueness of the solution). This is called generalized FACTOR
problem or n-FACTOR problem. In case n=2 we also say FACTOR problem
instead of 2-FACTOR problem.
Thecryptosystemsin[BKT11]arebasedonthe2-FACTORproblem. Stanek’s
modification of Shank’s baby-step giant-step algorithm solves this problem us-
(cid:112)
ingtimeandmemoryO( ord(g )ord(g )). Forpracticalpurposesitisdesirable
1 2
to reduce at least the memory requirements. This can be achieved by a simple
modification of Pollard’s kangaroo method presented in the next section.

2 Kangaroos solving the FACTOR problem
The connection between the discrete logarithm problem (DLP) and the FAC-
TORproblemwasalreadybroughtupin[BKT11]. AtleastafterStanek’swork
it is natural to look at other generic DLP-algorithms for possible adaptability
to the FACTOR problem. Since the iteration function in Pollard’s rho method
requires the calculation of powers of h = gx1gx2 we are stuck because of non-
1 2
commutativity1. But we have better luck with Pollard’s kangaroo algorithm.
For a detailed description of the original kangaroo algorithm see [Pol78].
We now describe the modified version (where we have no additional infor-
mation about the exponents x and x , see remarks below).
1 2
• Phase 0 - initialization:
Calculate ord(g ) and ord(g ), fix s ∈ N (in practice s ≈ 20) and define
1 2
(pseudorandom) partition functions
p :G→{1,...,s}
and
p :G→{1,...,s}
(cid:112) (cid:112)
Chooserandomconstantsu ,...,u ≈ ord(g )andv ,...,v ≈ ord(g ).
1 s 1 1 s 2
• Phase 1 - tame kangaroo:
Set T =e=g0g0 and dt =0,dt =0.
(cid:112) 1 2 1 2
Repeat (cid:100) ord(g )ord(g )(cid:101) times:
1 2
1. dt ←dt +u mod ord(g )
1 1 p1(T) 1
2. dt ←dt +v mod ord(g )
2 2 p2(T) 2
3. T ←g
up1(T)
·T ·g
vp2(T)
1 ·g
1 2 1 2
• Phase 2 - wild kangaroo:
Set W =h=gx1gx2 and dw =0,dw =0.
1 2 1 2
While W (cid:54)=T do
1. dw ←dw+u mod ord(g )
1 1 p1(W) 1
2. dw ←dw+v mod ord(g )
2 2 p2(W) 2
3. W ←g
up1(W)
·W ·g
vp2(W)
+x1
+x2
1 2 1 2
• Phase 3 - kangaroo collision:
If T =W we have
1 ·g
2 =T =W =g
+x1
+x2.
1 2 1 2
Thusx =dt −dw andx =dt −dw, sogx1 andgx2 areeasilycalculated.
1 1 1 2 2 2 1 2
Remark. • We note that the kangaroo method is a probabilistic algorithm.
(cid:112)
If there is no collision after e.g. 3(cid:100) ord(g )ord(g )(cid:101) steps in phase 2,
1 2
the attack should be restarted with different initialization values and/or
a different starting value for T.
1ThereisaPollard-rho-likealgorithmofBissonandSutherlandthatcanbeusedtosolve
theFACTORproblem,seetheremarkattheendofthissection.

• The original kangaroo method solves the discrete logarithm problem z =
(cid:112) √
yβ inexpectedrunningtimeO( ord(y))orevenO( γ−α)ifitisknown
that β ∈ [α,γ]. The analysis of our modified version can be done as in
(cid:112)
[Pol78] yielding an expected running time of O( ord(g )ord(g )), where
1 2
the algorithm can be improved in an obvious way if it is known that
x ∈[α ,γ ] and/or x ∈[α ,γ ].
1 1 1 2 2 2
• Revealing x and x the algorithm delivers more than we asked for.2
1 2
Remark. In an earlier version of this paper we claimed that there is no direct
way to extend both attacks, Stanek’s and ours, to solve the general FACTOR
problem. In fact this does not hold for the baby-step giant-step algorithm as
the version of Bisson and Sutherland in [BS11] shows. In the very same paper
BissonandSutherlandalsopresentaPollard-rho-likealgorithmforfindingshort
product representations in finite groups. The setting is as follows.
Let S = (s ,...,s ) be a (random) sequence of elements of a group G and
1 t
let z ∈G. If the sequence S satisfies t≥2log |G| the Pollard-rho algorithm of
Bisson and Sutherland finds a subsequence (s ,...,s ) of S with z =s ·...·
(cid:112)
i1 ir i1
s in expected running time O( |G|log |G|) using negligible memory. This
ir 2
method can be applied to solve the general FACTOR problem if we choose S
the following way:
• ForalliassembleasequenceS fromg ,g2,...g2bi whereb =(cid:100)log (ord(g ))(cid:101)
i i i i i 2 i
(tomakesurethatthereisasolution)andsufficientlymanyrandompow-
ers of g .
• For all i permute the elements of S in a random way.
• Build S by concatenation of S ,...,S .
1 n
Acknowledgements
Thanks to G.Bisson and A.Sutherland for pointing me to their work [BS11].
References
[BS11] G.Bisson, A.Sutherland, A low-memory algorithm for finding short
product representations in finite groups, to appear in Designs, Codes
and Cryptography, available at http://www.springerlink.com/
content/4293k3621h3316j7
[BKT11] S.Baba, S.Kotyada, R. Teja, A Non-Abelian Factorization Problem
and an Associated Cryptosystem, Cryptology ePrint Archive, Report
2011/048, 2011, http://eprint.iacr.org/2011/048.
[Pol78] J.Pollard, Monte Carlo methods for index computation mod p, Math-
ematics of Computation, Vol. 32, 1978.
[Sta11] M. Stanek, Extending Baby-step Giant-step algorithm for FACTOR
problem, Cryptology ePrint Archive, Report 2011/059, 2011, http:
//eprint.iacr.org/2011/059.
2InfacttheauthorisnotawareofanyalgorithmthatsolvestheFACTORproblemwithout
givingx1 andx2.