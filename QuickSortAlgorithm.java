public class QuickSortAlgorithm
{
	public static void main(String[] args)
	{
		int[] src = {26, 12, 31, 5, 14, 83, 29};
		quickSort(src, 0, src.length-1);
		for(int it : src)
		{
			System.out.print(it+" ");
		}
	}

	public static void quickSort(int[] src, int left, int right)
	{
		if (left < right)
		{
			int i = left;
			int j = right;
			int x = src[i];

			while(i < j)
			{
				while(i < j && x <= src[j])   //tips, i < j 
				{
					j--;
				}
				if(i < j)                     //tips, i < j 
				{
					src[i++] = src[j];
				}

				while(i < j && src[i] < x)    //tips,must be <
				{
					i++;
				}
				if(i<j)
				{
					src[j--] = src[i];
				}
			}
			src[i] = x;
			
			quickSort(src, left, i-1);
			quickSort(src, i+1, right);
		}
		
	}
}