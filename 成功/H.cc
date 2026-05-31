#include<bits/stdc++.h>
using namespace std;
struct Q{int l,r,x,i;}q[100005];
pair<int,int> e[100005];
int n,m,t,v[200005],b[200005],a[100005],c,k;
void U(int i){for(;i<=c;i+=i&-i)b[i]++;}
int S(int i){int s=0;for(;i;i-=i&-i)s+=b[i];return s;}
int main(){
ios::sync_with_stdio(0);cin.tie(0);
if(!(cin>>n>>m>>t))return 0;
for(int i=0;i<n;++i){cin>>e[i].first>>e[i].second;v[c++]=e[i].second;}
for(int i=0;i<m;++i){
cin>>q[i].l>>q[i].r>>q[i].x;q[i].i=i;
if(q[i].r-q[i].l<t){a[i]=-1;continue;}
q[i].l+=t;q[i].r-=t;v[c++]=q[i].l;
}
sort(v,v+c);c=unique(v,v+c)-v;
sort(e,e+n);
sort(q,q+m,[](Q x,Q y){return x.r<y.r;});
for(int i=0;i<m;++i){
if(a[q[i].i]==-1)continue;
while(k<n&&e[k].first<=q[i].r)U(lower_bound(v,v+c,e[k++].second)-v+1);
a[q[i].i]=(k-S(lower_bound(v,v+c,q[i].l)-v)>=q[i].x);
}
for(int i=0;i<m;++i)cout<<(a[i]==1?"Yes\n":"No\n");
}

