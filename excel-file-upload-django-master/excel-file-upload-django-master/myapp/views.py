from django.shortcuts import render
import pandas as pd


def index(request):
    if "GET" == request.method:
        return render(request, 'myapp/index.html', {})
    else:
        try:
            excel_file = request.FILES["excel_file"]
            is_private = request.POST.get('Sheetselection', False)
        
        

            df = pd.read_excel(excel_file,sheet_name=is_private)
        
       
        
            pd.set_option('display.max_columns', None)

            df2 = df[['Unnamed: 0','Unnamed: 14','Unnamed: 23','Unnamed: 18','Unnamed: 24','Unnamed: 15','Unnamed: 19','Unnamed: 31','Unnamed: 16']]
        
        
         
            excel_data = df2.shape


            df3 = df2.dropna(subset=['Unnamed: 0'])
            df3.drop([2,3],inplace=True)
            df3.reset_index().drop(['index'],axis=1)

            a = len(df3['Unnamed: 0'])

            df4 = df3.dropna(thresh=a,axis=1)
            df4.drop(['Unnamed: 0'],axis=1,inplace=True)
            df4

        #df3.drop([2,3],inplace=True)
            excel_data = []

            a = df4.columns
        
            for i in a:
                for j in df4[i]:
                    excel_data.append(j)

            return render(request, 'myapp/onsubmit.html', {"excel_data":excel_data})  
        
        except :
            s = "Something is Missing"
            return render(request, 'myapp/onsubmit.html',{"print":s})




        
        
        









