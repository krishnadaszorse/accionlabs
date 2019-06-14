inFile = 'input.txt' #input file
outFile = 'output.txt' #output file

# method for split lines in to a key and value, keys like '*','**','.','.'
def split_line(line):
  if len(line.split(' '))>1:
    return line.split(' ')[0],' '.join(line.split(' ')[1:])
  else:
    return None,None

# main method for read and write inut and output file
def main():
  input_file=open(inFile,'r')# opening input file in read mode
  output_file=open(outFile,'w')# opening output file in write mode
  data = input_file.readlines()# read all lines in txt file
  lines = [l for l in data if l.strip()!='']# remove all empty line
  count=1# start count numbering
  number='1'# start number
  bullet = ''# start bullet

  for x in range(0,len(lines)): # looping index of al lines
    if lines[x].strip()!='': 
      line=lines[x].strip()
      key,value = split_line(line)
      if key and key.startswith('*'):
        if key.count('*')==1:
          number = str(count)
          output_file.write(number+' '+value+'\n')
          count=count+1
        elif key.count('*')==number.count('.')+1:
          if number.count('.')>0:
            last_node=int(number.split('.')[-1])
            number='.'.join(number.split('.')[:-1]+[str(last_node+1)])
          else:
            number=str(count)+'.1'
          output_file.write(number+' '+value+'\n')
        elif key.count('*')==number.count('.')+2:
          number=number+'.1'
          output_file.write(number+' '+value+'\n')
        elif key.count('*')==number.count('.'):
          if number.count('.')>0:
            last_node=int(number.split('.')[-2])
            number='.'.join(number.split('.')[:-2]+[str(last_node+1)])
          else:
            number=str(count)+'.1'
          output_file.write(number+' '+value+'\n')
        else:
          if number.count('.')>0:
            last_node=int(number.split('.')[-number.count('.')])
            number='.'.join(number.split('.')[:-number.count('.')]+[str(last_node+1)])
          else:
            number=str(count)+'.1'
          output_file.write(number+' '+value+'\n')
      elif key and key.startswith('.'):
        nline=lines[x+1].strip() if len(lines)>x+1 else None
        if nline:
          nkey, nvalue = split_line(nline)
          if nkey and (key.count('.')<nkey.count('.') or not (nkey.startswith('*') or nkey.startswith('.'))):
            bullet=key.replace('.', ' ')+' +'
          else:
            bullet=key.replace('.', ' ')+' -'
        else:
          bullet=key.replace('.', ' ')+' -'
        output_file.write(bullet+' '+value+'\n')
      else:
        output_file.write(bullet.replace('+',' ').replace('-', ' ')+' '+str(value)+'\n')
  
  input_file.close()
  output_file.close()

main()