<h1 align="center">
	<img src="https://gmgn.ai/static/logo/GMGNLogo.webp" width="150px"><br>
    GMGN.ai Wrapper
</h1>
<p align="center">
	An API wrapper for undocumented endpoints at GMGN.ai<br>NOTE: This is for <b>MY</b> personal use, I do not condone the use of this API for any prohibited reason. :)</br>
</p>
<b>Example</b><br><br><br>

```python
from gmgn import gmgn

gmgn = gmgn()

getTokenInfo = gmgn.getTokenInfo(contractAddress="9eLRcHw2G4Ugrnp1p5165PuZsQ2YSc9GnBpGZS7Cpump")

print(getTokenInfo)
```
