using namespace std;
// Complete the timeInWords function below.
string timeInWords(int h, int m) {
    string number[30] = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "quarter", "sixteen", "seventeen", "eighteen", "nineteen", "twenty", "twenty one", "twenty two", "twenty three", "twenty four", "twenty five", "twenty six", "twenty seven", "twenty eight","twenty nine", "half"};

    //string time="";
    if(m==0)
        return number[h-1]+" o' clock";
    else if(m==15 || m==30)
        return number[m-1]+" past "+number[h-1];
    else if(m==1)
        return number[m-1]+" minute past "+number[h-1];
    else if(m<30)
        return number[m-1]+" minutes past "+number[h-1];
    else if(m==45)
        return number[59-m]+" to "+number[h];
    else if(m==59)
        return number[59-m]+" minute to "+number[h];
    else
        return number[59-m]+" minutes to "+number[h];        
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int h;
    cin >> h;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    int m;
    cin >> m;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    string result = timeInWords(h, m);

    fout << result << "\n";

    fout.close();

    return 0;
}
