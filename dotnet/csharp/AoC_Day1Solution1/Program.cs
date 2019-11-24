using System;
using System.IO;
using System.Collections.Generic;
//using System.Linq;

namespace AoC_Day1Solution1
{
    class Program
    {
        static void Main(string[] args)
        {
            List<int> Numbers = new List<int>();
            using ( StreamReader streamReader = new StreamReader("AoC_Day1Input.txt"))
            {
                while (streamReader.Peek() >=0){
                    Numbers.Add(Convert.ToInt32(streamReader.ReadLine()));
                }
            }
            int sum = 0;
            foreach (var item in Numbers)
            {
                sum += item;
            }
 //           int sum = Numbers.Sum(); // System.Linq necessary 
            Console.WriteLine(sum);           
        }
    }
}
