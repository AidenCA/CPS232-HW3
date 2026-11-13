# Part 3 — Fibonacci Heap Amortized Analysis

## Accounting method

A Fibonacci heap stores heap-ordered trees in a doubly linked root list and keeps a pointer to the minimum root. A node's degree is its number of children. A nonroot is marked after it loses its first child since being linked to its parent. If it loses another child while marked, it is cut and becomes a root.

Start with empty heaps and no credits. Keep **one credit on each root** and **two credits on each marked nonroot**. Each credit represents a fixed amount of work, chosen large enough to cover either a cut and its associated checks or a link and a constant amount of root processing. Each operation pays for its work using its new charge and any credits released from nodes. It also funds any new credits required by the rules. Since the balance starts at zero and never goes negative, the total charged over a sequence covers its actual running time.

## 1. Insert — O(1) amortized

Create a singleton root, add it to the root list, and update the minimum pointer if the new key is smaller or the heap was empty. The actual work is constant. Charge for that work and deposit one credit on the new root. The total charge is O(1).

## 2. Min — O(1) amortized

Read the minimum pointer and return the corresponding item, or report that the heap is empty. This takes constant time and changes no credits. The total charge is O(1).

## 3. Extract-min — O(log n) amortized

Remove the minimum root and promote its children to the root list. Consolidate by linking roots of equal degree, making the root with the larger key a child of the other root. A table indexed by degree tracks the roots during consolidation. After linking, scan the table to rebuild the root list and find the new minimum.

Let $r$ be the number of roots before extraction, $d$ the degree of the removed root, and $D$ an upper bound on the maximum degree during the operation. There are $r-1+d$ roots to process after promotion. If consolidation performs $L$ links and leaves $s$ roots, then

$$r-1+d=L+s.$$

Each link turns one root into a child. Spend that root's credit to pay for the link and one unit of root-list processing. The current operation pays for the processing of the $s$ surviving roots, which retain their credits. There is at most one survivor per degree, so $s$ is at most $D+1$. The current charge also covers removing the minimum, promoting the $d$ children and funding their root credits, and initializing and scanning the degree table. Marks on promoted nodes can be cleared and their old mark credits discarded. The total new charge is $O(1+d+s+D)=O(D+1)$. An empty heap can be handled in constant time.

### Why the degree bound is logarithmic

Consider a node with at least $k$ children. Number its current children in the order they were linked to it. When child $i$ was linked, the parent already had at least $i-1$ children. Roots are linked only at equal degrees, so child $i$ had degree at least $i-1$ at the time. It can lose at most one child while remaining attached to that parent. Its current degree is therefore at least $i-2$, or zero if $i-2$ is negative.

Let $F_0=0$, $F_1=1$, and $F_j=F_{j-1}+F_{j-2}$. By induction on $k$, a node with at least $k$ children has at least $F_{k+2}$ nodes in its subtree. For $k=0$, count the node itself. For $k=1$, count the node and its first child. For $k$ at least 2, count the parent, at least one node for the first child's subtree, and at least $F_i$ nodes for each child $i$ from 2 through $k$, using the induction hypothesis on degree $i-2$. This gives

$$1+1+\sum_{i=2}^{k} F_i=F_{k+2}.$$

Since Fibonacci numbers grow exponentially and the subtree has at most $n$ nodes, $D=O(\log n)$ for $n$ at least 2. Therefore, extract-min costs O(log n) amortized, with constant cost for heaps of size zero or one.

## 4. Decrease-key — O(1) amortized

Assume the operation receives a direct reference to the node. Lower its key and update the minimum pointer if needed. If the node is a root or its new key still satisfies heap order with its parent, the operation takes constant time and creates no new credit obligations.

If the new key is smaller than the parent's key, cut the node and add it to the root list. The parent has now lost a child. If the parent is a marked nonroot, cut it too and repeat the same check at its parent. If the cascade reaches an unmarked nonroot, mark it and stop. The cascade also stops at a root.

- The current operation pays for the first cut and deposits one root credit on the node it cuts. Any previous mark credits on that node can be discarded.
- Each subsequent cut removes a mark from a nonroot. Spend one of its two saved credits on the cut and keep the other as its new root credit.
- If the cascade ends by marking a node, deposit two credits on that node. At most one new mark is created.

The current charge covers constant initial work, at most one first cut, and at most one new mark. Saved credits cover the rest of the cuts, so the amortized cost is O(1).

## 5. Merge — O(1) amortized

Join the two doubly linked root lists using a constant number of pointer updates. Set the new minimum pointer to the smaller of the two minimums, or use the nonempty heap's pointer if only one heap is nonempty. The resulting heap takes ownership of both lists. Every root and marked nonroot carries its credits into the merged heap, so the charge covers only the constant actual work.

## Summary

| Operation | Amortized running time |
|---|---|
| Insert | O(1) |
| Min | O(1) |
| Extract-min | O(log n) |
| Decrease-key | O(1) |
| Merge | O(1) |

If delete is provided as a separate operation, decrease the target's key to a sentinel strictly below every other key and then extract it. The two operations together cost O(log n) amortized.

## References

- [MIT OpenCourseWare — Advanced Algorithms lecture notes](https://ocw.mit.edu/courses/6-854j-advanced-algorithms-fall-2008/16cda5a1eae18c7a26ec0c0498966dde_lec1.pdf)
- [University of Cambridge — Algorithms notes, §7.8](https://www.cl.cam.ac.uk/teaching/2021/Algorithms/notes2.pdf)
