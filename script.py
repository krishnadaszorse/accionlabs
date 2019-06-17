import sys

# method for split lines in to a key and value, keys like '*','**','.','.'
def split_line(line):
    if len(line.split(' '))>1:
        return line.split(' ')[0],' '.join(line.split(' ')[1:])
    else:
        return None,None

# main method for read and write inut and output file
def main():
    data = sys.stdin.readlines()# read all lines in txt file
    lines = [l for l in data if l.strip()!='']# remove all empty line
    count=1# start count numbering
    number='1'# start number
    bullet = ''# start bullet

    for x in range(0,len(lines)): # looping index of al lines
        line=lines[x].strip()# for strip \n from line
        key,value = split_line(line)# callsplitline function for split it like key, value
        if key and key.startswith('*'):# checking key start from *
            if key.count('*')==1:# checking key start from *
                number = str(count)
                sys.stdout.write(number+' '+value+'\n')
                count=count+1
            elif key.count('*')==number.count('.')+1:
                if number.count('.')>0:
                    last_node=int(number.split('.')[-1])
                    number='.'.join(
                        number.split('.')[:-1]
                        +[str(last_node+1)])
                else:
                    number=str(count)+'.1'
                sys.stdout.write(number+' '+value+'\n')
            elif key.count('*')==number.count('.')+2:
                number=number+'.1'
                sys.stdout.write(number+' '+value+'\n')
            elif key.count('*')==number.count('.'):
                if number.count('.')>0:
                    last_node=int(number.split('.')[-2])
                    number='.'.join(
                        number.split('.')[:-2]
                        +[str(last_node+1)])
                else:
                    number=str(count)+'.1'
                sys.stdout.write(number+' '+value+'\n')
            else:
                if number.count('.')>0:
                    last_node=int(
                        number.split('.')[-number.count('.')])
                    number='.'.join(
                        number.split('.')[:-number.count('.')]
                        +[str(last_node+1)])
                else:
                    number=str(count)+'.1'
                sys.stdout.write(number+' '+value+'\n')
        elif key and key.startswith('.'):
            nline=lines[x+1].strip() if len(lines)>x+1 else None
            if nline:
                nkey, nvalue = split_line(nline)
                if (nkey and 
                        (key.count('.')<nkey.count('.') or not
                        (nkey.startswith('*') or 
                        nkey.startswith('.')))):
                    bullet=key.replace('.', ' ')+' +'
                else:
                    bullet=key.replace('.', ' ')+' -'
            else:
                bullet=key.replace('.', ' ')+' -'
            sys.stdout.write(bullet+' '+value+'\n')
        else:
            sys.stdout.write(
                bullet.replace('+',' ').replace('-', ' ')
                +' '+str(value)+'\n')

main()