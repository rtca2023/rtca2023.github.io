---
layout: default
page_site: Lyon 
page_id: 1
---

**Registration is open:** [indico.math.cnrs.fr M3 workshop](https://indico.math.cnrs.fr/event/9802/)

**Contact:** [rtca2023@listes.ens-lyon.fr](mailto:rtca2023@listes.ens-lyon.fr)

### Mathematical Software and High Performance Algebraic Computing

*June 26 to 30, 2023*

**Location:**  [ENS de Lyon, site Monod](http://www.ens-lyon.fr/en/campus-life/campus-tour/maps-directions).

[Practical information (thanks to Nicolas Brisebarre)](https://perso.ens-lyon.fr/nicolas.brisebarre/lyon_hints.html)

**Organizers:**  [W. Decker](https://math.rptu.de/en/wgs/agag/people/head/decker), [J.-G. Dumas](https://ljk.imag.fr/membres/Jean-Guillaume.Dumas), [C. Pernet](https://ljk.imag.fr/membres/Clement.Pernet), [E. Thomé](https://members.loria.fr/EThome), [G. Villard](https://perso.ens-lyon.fr/gilles.villard)

At present the practical organization of this workshop is partly 
prospective since in particular we plan to couple the event with developer days 
from various software groups. This ranges from many specialized opensource components (ex: FLINT, FpLLL, LinBox, etc.), to thematic systems (ex: GAP, Pari/GP, Singular, etc.) and general purpose ones (ex: OSCAR, Mathemagix, SageMath, etc.). We also plan to have a participation of MapleSoft and Wolfram Mathematica.  
The goal of the workshop is to allow the software actors to present what the existing software systems are, with general and introductory talks, and focus on the latest advances and perspectives. 
We also aim at making links between communities by 
inviting representatives of interface softwares such as jupyter and Julia, and from research around interoperability formats and OpenMath.

A specific interest will be for the advancement of optimized code and parallel software in all areas of symbolic mathematical computation. Research challenges also concern interfaces and integration of components, JIT compilation and metaprogramming. At the 
algorithmic and application level, mastering precisions and hybrid symbolic, certified 
and numerical methods requires complex environments and sophisticated software implementations. New applications, computational challenges and experimental mathematics problems should be raised to open up new perspectives for the design of computer algebra softwares. 

A round table meeting will be held for addressing issues around the promotion of software skills for scientific careers, including academic ones. 

**Preliminary Program**



<table>
<tbody>
	<!-----------     MONDAY ---------------------------------------------->
<tr>
      <th style="width:10%"> </th>
      <th style="width:20%" style="text-align: center"> </th>
      <th style="width:70%">Monday June 26th, 2023</th>
</tr>
<tr>
    <td> 12:30-13:45</td><td></td><td> Lunch break </td>
</tr>
<tr>
    <td> 13:45-14:00</td><td></td><td> Opening </td>
</tr>
<tr>
    <td> 14:00-15:00</td>
    <td><a href="https://fredrikj.net">Fredrik Johansson</a></td>
    <td></td>
</tr>
<tr>
    <td> 15:00-16:00 </td>
    <td><a href="https://www.math.u-bordeaux.fr/~ballombe">Bill Allombert</a></td>
    <td></td>
</tr>
<tr>
    <td> 16:00-16:30</td><td></td><td> Coffee break </td>
</tr>
<tr>
    <td> 16:30-17:30</td>
    <td><a href="https://www.lisn.upsaclay.fr/members/thiery-nicolas/">Nicolas Thiéry</a></td>
    <td></td>
</tr>
    <!-----------     TUESDAY  ---------------------------------------------->
<tr>
      <th style="width:10%"> </th>
      <th style="width:20%" style="text-align: center"> </th>
      <th style="width:70%">Tuesday June 27th, 2023</th>
</tr>
<tr>
    <td> 9:00-10:00</td>
    <td>Keegan Ryan</td>
    <td><details><summary>Fast Practical Lattice Reduction through Iterated Compression</summary>
        <blockquote>We introduce a new lattice basis reduction algorithm with approximation guarantees analogous to the LLL algorithm and practical performance that far exceeds the current state of the art. We achieve these results by iteratively applying precision management techniques within a recursive algorithm structure and show the stability of this approach. We analyze the asymptotic behavior of our algorithm, and show that the heuristic running time is $O(n^{\omega}(C+n)^{1+\varepsilon})$ for lattices of dimension $n$, $\omega\in (2,3]$ bounding the cost of size reduction, matrix multiplication, and QR factorization, and $C$ bounding the log of the condition number of the input basis $B$. This yields a running time of $O\left(n^\omega (p + n)^{1 + \varepsilon}\right)$ for precision $p = O(\log \|B\|_{max})$ in common applications. Our algorithm is fully practical, and we have published our implementation. We experimentally validate our heuristic, give extensive benchmarks against numerous classes of cryptographic lattices, and show that our algorithm significantly outperforms existing implementations.
</blockquote>
</details></td>
</tr>
<tr>
    <td> 10:00-11:00</td>
    <td><a href="https://math.rptu.de/en/wgs/agag/people/head/decker">Wolfram Decker</a></td>
    <td></td>
</tr>
<tr>
    <td> 11:00-11:30</td><td></td><td> Coffee break </td>
</tr>
<tr>
    <td> (11:30-12:30)</td>
    <td><a href="http://www.normalesup.org/~page/index.html">Aurel Page</a></td>
    <td></td>
</tr>
<tr>
    <td> 12:30-14:00</td><td></td><td> Lunch break </td>
</tr>
<tr>
    <td> 14:00-15:00</td>
    <td><a href="https://www.texmacs.org/joris/main/joris.html">Joris van der Hoeven</a></td>
    <td></td>
</tr>
<tr>
    <td> (15:00-16:00) </td>
    <td><a href="https://members.loria.fr/EThome/">Emmanuel Thomé</a></td>
    <td></td>
</tr>
<tr>
    <td> 16:00-16:30</td><td></td><td> Coffee break </td>
</tr>
<tr>
    <td> 16:30</td><td></td><td> Sprint </td>
</tr>
    <!-----------     WEDNESDAY ---------------------------------------------->
<tr>
      <th style="width:10%"> </th>
      <th style="width:20%" style="text-align: center"> </th>
      <th style="width:70%">Wednesday 28th, 2023</th>
</tr>
<tr>
    <td> 9:00-10:00 </td>
    <td><a href="https://defeo.lu">Luca De Feo</a></td>
    <td></td>
</tr>
<tr>
    <td> 10:00-11:00 </td>
    <td><a href="https://math.rptu.de/ags/agag/personen/leitung/fieker">Claus Fieker</a></td>
    <td></td>
</tr>

<tr>
    <td> 11:00-11:30</td><td></td><td> Coffee break </td>
</tr>
<tr>
    <td> 11:30-12:30 </td>
    <td><a href="http://www.iaa.tu-bs.de/beick/">Bettina Eick</a></td>
    <td></td>
</tr>
<tr>
    <td> 12:30-14:00</td><td></td><td> Lunch break </td>
</tr>
<tr>
    <td> 14:00-15:00 </td>
    <td><a href="https://antonleykin.math.gatech.edu">Anton Leykin</a></td>
    <td></td>
</tr>
<tr>
    <td> 15:00-16:00 </td>
    <td><a href="https://membres-ljk.imag.fr/Jean-Guillaume.Dumas/">Jean-Guillaume Dumas</a></td>
    <td></td>
</tr>
<tr>
    <td> 16:00-16:30</td><td></td><td> Coffee break </td>
</tr>
<tr>
    <td> 16:30</td><td></td><td> Sprint </td>
</tr>
<tr>
    <td> 19:30</td><td></td><td> Dinner </td>
</tr>
    <!-----------     THURSDAY  ---------------------------------------------->
<tr>
      <th style="width:10%"> </th>
      <th style="width:20%" style="text-align: center"> </th>
      <th style="width:70%">Thursday 29th, 2023</th>
</tr>
<tr>
    <td> 9:00-10:00 </td>
    <td><a href="https://www.dima.unige.it/~bigatti/">Anna Maria Bigatti</a></td>
    <td></td>
</tr>
<tr>
    <td> 10:00-11:00 </td>
    <td><a href="https://www.fil.univ-lille.fr/~lemairef/homepage/index.php">François Lemaire</a></td>
    <td><details><summary>The DifferentialAlgebra project</summary>
        <blockquote>The DifferentialAlgebra project, lead by François Boulier, aims at
providing BLAD, a C library dedicated to Ritt and Kolchin differential
algebra, and BMI, a library providing interface packages for various
scientific computing software such as Maple, Sagemath, Python / Sympy...

Recent functionalities will be presented through several applications
of differential algebra technics (quasi-equilibrium approximation,
fraction decoupling, ...).

URL: <a href="https://codeberg.org/francois.boulier/DifferentialAlgebra">https://codeberg.org/francois.boulier/DifferentialAlgebra</a>

</blockquote>
</details></td>
</tr>
<tr>
    <td> 11:00-11:30</td><td></td><td> Coffee break </td>
</tr>
<tr>
    <td> 11:30-12:30 </td>
    <td><a href="https://www.csd.uwo.ca/~mmorenom/homepage-moreno.html">Marc Moreno Maza</a></td>
    <td></td>
</tr>
<tr>
    <td> 12:30-14:00</td><td></td><td> Lunch break </td>
</tr>
<tr>
    <td> 14:00-15:00 </td>
    <td><a href="https://www-polsys.lip6.fr/~safey/">Mohab Safey El Din</a></td>
    <td></td>
</tr>
<tr>
    <td> 15:00-16:00 </td>
    <td><a href="https://www.lirmm.fr/~giorgi/">Pascal Giorgi</a></td>
    <td></td>
</tr>
<tr>
    <td> 16:00-16:30</td><td></td><td> Coffee break </td>
</tr>
<tr>
    <td> 16:30</td><td></td><td> Sprint </td>
</tr>
    <!-----------     FRIDAY ---------------------------------------------->
<tr>
      <th style="width:10%"> </th>
      <th style="width:20%" style="text-align: center"> </th>
      <th style="width:70%">Friday 30th, 2023</th>
</tr>
<tr>
    <td> 9:00-10:00 </td>
    <td><a href="http://www.lix.polytechnique.fr/Labo/Gleb.POGUDIN/">Gleb Pugudin</a></td>
    <td></td>
</tr>
<tr>
    <td> 10:00-11:00 </td>
    <td><a href="http://perso.ens-lyon.fr/jean-yves.l.excellent/">Jean-Yves L'Excellent</a></td>
    <td><details><summary>Sparse direct solvers and HPC</summary>
        <blockquote>The solution of sparse systems of linear equations is a key computational kernel in scientific
   computing. It often represents the most time, memory and energy consuming part of the whole
   numerical simulation process. Therefore, it is critical to design efficient sparse solvers.

   In this talk, we focus on sparse direct solvers, which are well-known for their numerical
   robustness and accuracy. We present recent key features of sparse direct solvers that enable
   to efficiently solve large real and complex systems, and that have led to a strong gain of
   interest of these methods in many applications. We also illustrate how today challenges
   related to heterogeneity of computers, energy control, mixed-precision arithmetics, new models
   and applications, motivate new research in the field of sparse direct solvers. We finally
   mention how the sparse direct solver MUMPS is supported by research and industrial collaborations.
</blockquote>
</details></td>
</tr>

<tr>
    <td> 11:00-11:30</td><td></td><td> Coffee break </td>
</tr>
<tr>
    <td> 11:30-12:30 </td>
    <td><a href="https://www.quendi.de/en/math.html">Max Horn</a></td>
    <td></td>
</tr>
<tr>
    <td> 12:30-14:00</td><td></td><td> Lunch and end of the workshop</td>
</tr>
</tbody>
</table>


**[Code of Conduct]({% link code_of_conduct.md %})**



