from django.shortcuts import render
from django.http import HttpResponse
import re
# Create your views here.
def index(request):
    res=render(request,'index.html')
    return res

def calc(request):
    final_result = ''
    values = ''
    error = ''
    try:
        if request.method=="POST":
            values=request.POST['values']
            print(values)
            vals=re.findall(r"\d+",values)
            operators=['+','x','÷','.','-','%']
            opr=[]

        for v in values:
            for o in operators:
                if v==o:
                    opr.append(o)

        for o in opr:
            if o=='.':
                i=opr.index(o)
                print(i)
                if i == 0:
                    res=vals[0]+"."+vals[1]         
                    vals.remove(vals[1])
                    opr.remove(opr[i])
                    vals[0]=res
                else:
                    res=vals[1]+"."+vals[2]
                    vals.remove(vals[2])
                    opr.remove(opr[i])
                    vals[1]=res
        
        for o in opr:
            if o=='%':
                i=opr.index(o)
                res=(float(vals[0])/100)*float(vals[1])
                vals.remove(vals[1])
                opr.remove(opr[i])
                vals[0]=res

        for o in opr:
            if o=='÷':
                i=opr.index(o)
                res=float(vals[0])/float(vals[1])
                vals.remove(vals[1])
                opr.remove(opr[i])
                vals[0]=str(res)
                
        for o in opr:
            if o=='x':
                i=opr.index(o)
                res=float(vals[0])*float(vals[1])
                vals.remove(vals[1])
                opr.remove(opr[i])
                vals[0]=str(res)
                
        for o in opr:
            if o=='+':
                i=opr.index(o)
                res=float(vals[0])+float(vals[1])
                vals.remove(vals[1])
                opr.remove(opr[i])
                vals[0]=str(res)

            if o=='-':
                i=opr.index(o)
                res=float(vals[0])-float(vals[1])
                vals.remove(vals[1])
                opr.remove(opr[i])
                vals[0]=str(res)

        if len(opr)!=0:
            if opr[0]=='÷':
                result = float(vals[0])/float(vals[1])
            elif opr[0]=='x':
                result = float(vals[0])*float(vals[1])
            elif opr[0]=='+':
                result = float(vals[0])+float(vals[1])
            else :
                result = float(vals[0])-float(vals[1])
        else:
            result = float(vals[0])

        final_result=round(result,2)
        print(final_result)
    except Exception as e:
        error = str(e)
    res=render(request,'index.html',{'result':final_result,'values':values, 'errors': error})
    return res
