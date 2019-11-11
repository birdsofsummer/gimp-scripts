fs=require('fs')
R=require('ramda')
c=require('cheerio')
s=require('superagent')

download=async (u)=>{
    r=await s.get(u)
    $=c.load(r.text)
    img=$('img')
    z=R.range(0,img.length).map(i=>img.eq(i).attr('src'))
    R.map(x=>[x,x.split('/').slice(-1)[0]],z)
     .map(([u,n])=>s.get(u).pipe(fs.createWriteStream(n)))
}

u=`https://www.douban.com/group/topic/151967567/`
download(u)
