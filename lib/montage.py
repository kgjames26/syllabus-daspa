import sys, glob
from PIL import Image
def montage(folder, out, cols=4, start=0, count=8):
    fs = sorted(glob.glob(folder+'/p-*.png'), key=lambda x:int(x.split('-')[-1][:-4]))[start:start+count]
    ims=[Image.open(f) for f in fs]; w,h=ims[0].size
    rows=(len(ims)+cols-1)//cols
    M=Image.new('RGB',(cols*w+(cols-1)*6, rows*h+(rows-1)*6),'#888')
    for i,im in enumerate(ims): M.paste(im,((i%cols)*(w+6),(i//cols)*(h+6)))
    M.save(out)
if __name__=='__main__': montage(sys.argv[1],sys.argv[2],int(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5]))
