namespace Thesis2020.Examples
{
    using System;
    using System.Collections.Generic;
    using System.Linq;

    class Examples
    {
        public void Test()
        {
            int[] array = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

            // Teil aus dem array wird kopiert (3, 4, 5).
            int[] part = array.Skip(2).Take(3).ToArray();

            Console.WriteLine("[{0}]", string.Join(", ", part));
            part[2] = 99;
            Console.WriteLine("[{0}]", string.Join(", ", part));

            Console.WriteLine("[{0}]", string.Join(", ", array.ToArray()));
        }


        public void Test2()
        {
            Span<int> span = new[] {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}.AsSpan();

            // Teil aus dem array wird referenziert (3, 4, 5).
            Span<int> part = span.Slice(2, 3);

            Console.WriteLine("[{0}]", string.Join(", ", part.ToArray()));
            part[2] = 99;
            Console.WriteLine("[{0}]", string.Join(", ", part.ToArray()));

            Console.WriteLine("[{0}]", string.Join(", ", span.ToArray()));

            Test5(part);
            Console.WriteLine("[{0}]", string.Join(", ", part.ToArray()));
        }

        public void Test3()
        {
            List<int> list = new[] { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 }.ToList();

            // Teil aus dem array wird referenziert (3, 4, 5).
            List<int> part = list.Skip(2).Take(3).ToList();

            Console.WriteLine("[{0}]", string.Join(", ", part.ToArray()));
            part[2] = 99;
            Console.WriteLine("[{0}]", string.Join(", ", part.ToArray()));

            Console.WriteLine("[{0}]", string.Join(", ", list.ToArray()));
        }

        public void Test4()
        {
            Memory<int> memory = new[] { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 }.AsMemory();

            // Teil aus dem array wird referenziert (3, 4, 5).
            Memory<int> part = memory.Slice(2,3);

            Console.WriteLine("[{0}]", string.Join(", ", part.ToArray()));
            part.Span[2] = 99;
            Console.WriteLine("[{0}]", string.Join(", ", part.ToArray()));

            Console.WriteLine("[{0}]", string.Join(", ", memory.ToArray()));
        }

        public void Test5(Span<int> test)
        {
            test[0] = 88;
        }

    }
}
