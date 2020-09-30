import FN
import CF
import os

if  __name__ == '__main__':
    fn1 = FN.FN(r'H:\OneDrive - revolutionize B2C bandwidth\视频教程\架构H:\OneDrive - revolutionize B2C bandwidth\视频教程\架构')
    fn1.analyzeExtensions()
    d = fn1.filesNum
    d = sorted(d.items(), key=lambda item: item[1], reverse=True)
    '''
    这里的d.items()实际上是将d转换为可迭代对象，
    迭代对象的元素为 （‘lilee’,25）、（‘wangyan’,21）、（‘liqun’,32）、（‘lidaming’,19），
    items()方法将字典的元素 转化为了元组，
    而这里key参数对应的lambda表达式的意思则是选取元组中的第二个元素作为比较参数
    （如果写作key=lambda item:item[0]的话则是选取第一个元素作为比较对象，也就是key值作为比较对象。
    lambda x:y中x表示输出参数，y表示lambda 函数的返回值），
    所以采用这种方法可以对字典的value进行排序。
    注意排序后的返回值是一个list，而原字典中的名值对被转换为了list中的元组。
    '''
    print(d)
