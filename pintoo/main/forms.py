from django import forms

from main.models import Commodity, Pintoo, Transport, Number


class CommodityForm(forms.ModelForm):
    commodity = forms.CharField(label='標題', max_length=128)
    pintoo = forms.ModelChoiceField(label='類型', queryset=Pintoo.objects.all(), widget=forms.Select)
    image1 = forms.ImageField(label='圖片1', required=False)
    image2 = forms.ImageField(label='圖片2', required=False)

    class Meta:
        model = Commodity
        fields = '__all__'
        
        
class CommodityBuyForm(forms.ModelForm):
    name = forms.CharField(label='姓名', max_length=128)
    number = forms.CharField(label='電話號碼', max_length=128)
    eMail = forms.EmailField(label='信箱', widget=forms.TextInput())
    transport = forms.ModelChoiceField(label='運送方式', queryset=Transport.objects.all(), widget=forms.Select)
    adress = forms.CharField(label='地址', max_length=128)
    forms.CharField(label='內容', widget=forms.Textarea, required=False)

    class Meta:
        model = Number
        fields = '__all__'