import java.util.*;

public class program{
    public static void main(String args[]){
        Scanner key = new Scanner(System.in);
        System.out.format("Enter array size\n");
        int size = key.nextInt();
        int[] arr = new int[size];

        System.out.format("Enter numbers to fill array\n");
        for (int i = 0; i < size; i++){
            int ele = key.nextInt();
            arr[i] = ele;
        }
        System.out.format("Enter search\n");
        int search = key.nextInt();
        // 1)
        lSearch(arr, size, search);
        // 2)
        bSearch(arr, size, search);
    }

    // 1)
    static void lSearch(int[] arr, int size, int search){
        for (int i = 0; i < size; i++){
            if (search == arr[i]){
                System.out.format("lSearch -> match on index: %d\n", i);
                return;
            }
        }
        System.out.format("lSearch -> not found in the array\n");
        return;
    }
    // 2)
    static void bSearch(int[] arr, int size, int search){
        int val = -1;
        int head = 0;
        int tail = size-1;
        while (head <= tail){
            int mid = (head + tail)/2;
            if (arr[mid] == search){
                val = mid;
                break;
            }
            else if (mid < search){
                head = mid;
            }
            else{
                tail = mid;
            }
        }
        if (val == -1){
            System.out.format("lSearch -> not found in the array\n");
            return;
        }
        System.out.format("bSearch -> match on index: %d\n", val);
        return;
    }
}

// 3) Because i couldn't be bothered to hand in a PDF besides
// [2,1,4], i = 0
//
// SOL
//
// index = 0
// index = 1
// smallerNumber = 1
// [1,2,4]
//
//      index = 1
//      smallerNumber = 2
//      [1,2,4]
//
//              EOL
