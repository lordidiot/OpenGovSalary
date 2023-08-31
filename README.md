# OpenGovSalary

Open Government Products ([OGP](https://www.open.gov.sg/)) maintains a list of their [products](https://www.open.gov.sg/products/) and the corresponding operational costs involved.
These costs include manpower costs, alongside a detailed breakdown of the contribution of each member.

This is great demonstration of transparency that I would like to commend.
Interestingly, this information is enough to form a system of linear equations in terms of each OGP employee's salary.
Should we find a good solution to this system of linear equations, we can approximate the salary of each employee.

## Set-up

You will need an installation of python3 with `venv`.

```bash
python3 -m venv .env
source .env/bin/activate
python script.py
```

## Sample output

Here is a sample output, generated from data available on 31082023.

```
Found exact solution:

weeloong: $267,189/year
ian: $267,189/year
alwyn: $224,927/year
antariksh: $224,924/year
christabelpng: $223,665/year
sihan: $223,665/year
khant: $223,665/year
geraldine: $223,665/year
yongjie: $223,665/year
kokseng: $220,715/year
veena: $220,715/year
prawira: $220,715/year
jiehao: $220,715/year
yuanruo: $220,715/year
enyi: $200,893/year
angel: $200,893/year
cheri: $200,893/year
tiffany: $200,893/year
kenneth: $200,893/year
nicholasng: $200,893/year
dat: $199,041/year
hena: $199,041/year
prakriti: $197,824/year
alexis: $197,824/year
ziwei: $197,609/year
chinyang: $193,274/year
moses: $193,274/year
sheikh: $193,274/year
stacey: $192,113/year
kevan: $184,138/year
reshma: $184,138/year
alexander: $183,531/year
kishore: $183,531/year
qilu: $183,531/year
jan: $183,531/year
natalie: $183,531/year
jiachin: $183,531/year
shazli: $183,531/year
harish: $183,531/year
feliciana: $181,736/year
carina: $180,557/year
fabian: $180,557/year
charmaine: $180,557/year
sean: $180,557/year
weilun: $177,516/year
ivan: $177,516/year
kaiwen: $177,465/year
pete: $175,839/year
jason: $175,839/year
zeke: $175,839/year
mayying: $174,322/year
jennifer: $174,322/year
khaleedah: $174,322/year
yixin: $167,981/year
ajayraj: $162,496/year
ziyang: $162,496/year
latasha: $162,496/year
rachel: $162,496/year
arshad: $162,496/year
jessendra: $162,496/year
louiz: $156,061/year
jasmine: $156,061/year
huiling: $156,061/year
caleb: $156,061/year
daryl: $156,061/year
kahhow: $156,061/year
adan: $156,061/year
jingyi: $156,061/year
jenwei: $156,061/year
kennethchang: $154,574/year
shuli: $154,574/year
huiqing: $154,574/year
amit: $154,574/year
sebastian: $154,574/year
justyn: $154,574/year
ken: $154,574/year
chifa: $154,574/year
wanling: $154,574/year
kishen: $151,823/year
paul: $151,823/year
kendra: $151,823/year
jiayee: $151,823/year
raisa: $149,110/year
nitya: $140,588/year
suhaila: $133,928/year
oliver: $133,928/year
stephanie: $114,351/year
syan: $111,832/year
talitha: $108,715/year
jieyin: $87,919/year
clement: $78,120/year
simun: $64,510/year
shawn: $52,020/year
pallani: $50,607/year
```

## ⚠️ Disclaimer

Doing a cursory look through the output, there do seem to be some inaccuracies (e.g. a senior engineer with a much lower compensation than others).
Therefore, please only think of this project as a proof-of-concept meant to explore the idea of uncovering the salaries, but not results you can fully trust.