using System;
using System.Runtime.InteropServices;

namespace playground
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");

            var message = "Test 123123123";
            var span = message.AsSpan();

            Span<byte> bytes = stackalloc byte[2]; // Using C# 7.2 stackalloc support for spans
            bytes[0] = 42;
            bytes[1] = 43;
            // Assert.Equal(42, bytes[0]);
            // Assert.Equal(43, bytes[1]);
            bytes[2] = 44; // throws IndexOutOfRangeException
        }
    }
}
