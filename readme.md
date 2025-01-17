# Аналіз алгоритмів пошуку шляхів у графі

У цьому проекті ми реалізували алгоритми пошуку шляхів у графі за допомогою Depth-First Search (DFS) та Breadth-First Search (BFS). Для цього ми скористалися бібліотекою NetworkX для моделювання графа.

## Опис графа
Наш граф представляє собою корпоративну мережу, де присутні різні мережеві пристрої, такі як роутери, комутатори, комп'ютери та принтери. Вершинами графа є ці пристрої, а ребра позначають зв'язки між ними.

## Реалізація алгоритмів пошуку шляхів
Ми реалізували два алгоритми пошуку шляхів: DFS та BFS. DFS шукає шляхи глибше в глибину, в той час як BFS шукає шляхи ширше в ширину. Для обох алгоритмів ми створили функції `dfs_paths` та `bfs_paths`, які знаходять всі можливі шляхи між двома заданими вершинами.

## Результати виконання
Ми порівняли результати виконання обох алгоритмів для пошуку шляхів між двома конкретними пристроями: Router1 та PC2. Для кожного алгоритму були знайдені шляхи, і ми порівняли їх результати.

## Висновки
В результаті порівняння ми помітили, що DFS та BFS можуть знайти різні шляхи між заданими вершинами в графі. Це відбувається через різницю у стратегіях обходу графа: глибокий пошук просувається якнайдалі в одну гілку перед тим, як повернутися, тоді як широкий пошук відвідує всі сусідні вершини на поточному рівні перед тим, як переходити на наступний рівень. Вибір алгоритму залежить від конкретних потреб і властивостей графа.

У нашому випадку обидва алгоритми мають свої переваги: DFS може бути ефективним для знаходження шляхів у глибоких гілках графа, тоді як BFS може бути корисним для знаходження шляхів, що проходять через різні гілки графа.
