from django import template
register = template.Library()
def ench(str,num):
        num = int(num)
        try:
                value = str.split('/')[num]
        except IndexError:
                value = str.split('/')[0]
        return value
register.filter('ench',ench)