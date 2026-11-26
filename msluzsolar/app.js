(function(){
 const fmt=v=>v.toLocaleString('pt-BR',{style:'currency',currency:'BRL',maximumFractionDigits:0});
 const inp=document.getElementById('conta'),rng=document.getElementById('contaR');
 if(!inp)return;
 let tipo='residencial';
 // Premissas conservadoras (estimativa): tarifa média c/ impostos ~R$ 1,00/kWh; geração média ~120 kWh/mês por kWp no DF/GO;
 // economia de 75% a 90% do valor da conta (permanecem taxa mínima, iluminação pública e encargos de rede).
 function calc(){
  let v=parseFloat(String(inp.value).replace(/\D/g,''))||0;
  const kwh=v/1.0, kwp=Math.max(kwh/120,0), placas=Math.ceil(kwp*1000/580);
  const eMin=v*.75, eMax=v*.90;
  document.getElementById('rMes').textContent=v?fmt(eMin)+' a '+fmt(eMax):'—';
  document.getElementById('rAno').textContent=v?fmt(eMin*12)+'+':'—';
  document.getElementById('r25').textContent=v?fmt(eMin*12*25)+'+':'—';
  document.getElementById('rKwp').textContent=v?kwp.toFixed(1).replace('.',',')+' kWp':'—';
  document.getElementById('rPlacas').textContent=v?('≈ '+placas+' placas'):'—';
  const msg=`Olá! Fiz a simulação no site da MS Luz Solar. Minha conta de luz é de ${fmt(v)} por mês (${tipo}). Quero uma proposta de energia solar.`;
  document.getElementById('simWa').href='https://wa.me/5561981214135?text='+encodeURIComponent(msg);
 }
 inp.addEventListener('input',()=>{rng.value=parseFloat(inp.value.replace(/\D/g,''))||0;calc()});
 rng.addEventListener('input',()=>{inp.value=rng.value;calc()});
 document.querySelectorAll('.seg button').forEach(b=>b.addEventListener('click',()=>{
  document.querySelectorAll('.seg button').forEach(x=>x.setAttribute('aria-pressed','false'));
  b.setAttribute('aria-pressed','true');tipo=b.dataset.t;calc();}));
 calc();
 const f=document.getElementById('orc');
 const WEBHOOK='https://hook.us2.make.com/gjjw1e8e20fba1ljsn7djqrvyji3e2un';
 f&&f.addEventListener('submit',e=>{e.preventDefault();
  const st=document.getElementById('orc-st'),btn=f.querySelector('button[type=submit]');
  if(f.empresa_site.value)return;
  let tel=f.telefone.value.replace(/\D/g,'');if(tel.indexOf('55')!==0)tel='55'+tel;
  if(!f.nome.value.trim()||!f.aceite.checked||tel.length<12||tel.length>13||!f.valor.value.trim()){st.textContent='Confira nome, telefone, valor da conta e o aceite.';return;}
  const d=new FormData(f);
  const msg=`Olá! Quero uma simulação de energia solar.\nNome: ${d.get('nome')}\nCidade: ${d.get('cidade')}\nTipo de imóvel: ${d.get('tipo')}\nValor médio da conta: R$ ${d.get('valor')}${d.get('obs')?'\nObs.: '+d.get('obs'):''}`;
  const wa='https://wa.me/5561981214135?text='+encodeURIComponent(msg);
  const p=new URLSearchParams({empresa:'MS Luz Solar',nome:f.nome.value.trim(),telefone:tel,cidade:d.get('cidade'),
   tipo_servico:'Energia solar - '+d.get('tipo'),valor_conta:d.get('valor'),obs:d.get('obs')||'',origem:location.href,
   gclid:new URLSearchParams(location.search).get('gclid')||'',data_envio:new Date().toISOString()});
  btn.disabled=true;st.textContent='Enviando...';
  const c=new AbortController(),t=setTimeout(()=>c.abort(),8000);
  fetch(WEBHOOK,{method:'POST',mode:'no-cors',body:p,signal:c.signal})
   .then(()=>{st.innerHTML='Recebemos sua solicitação! Para agilizar, <a href="'+wa+'" target="_blank" rel="noopener">continue no WhatsApp</a>.';f.reset();
     if(window.gtag)gtag('event','conversion',{'send_to':'AW-11471703423/8kKYCIWuragdEP-akd4q'});if(window.gtag)gtag('event','generate_lead',{empresa:'MS Luz Solar'});})
   .catch(()=>{st.textContent='Abrindo o WhatsApp para você...';window.open(wa,'_blank');})
   .finally(()=>{clearTimeout(t);btn.disabled=false;});});
 // conversões: cliques no WhatsApp e no telefone (mesmas ações do Google Ads da MS)
 document.addEventListener('click',e=>{const a=e.target.closest&&e.target.closest('a[href]');if(!a||typeof gtag!=='function')return;
  const h=a.getAttribute('href')||'';
  if(h.indexOf('https://wa.me/')===0)gtag('event','conversion',{'send_to':'AW-11471703423/no1fCM-0yZIdEP-akd4q'});
  else if(h.indexOf('tel:')===0)gtag('event','conversion',{'send_to':'AW-11471703423/o9v9CNK0yZIdEP-akd4q'});},true);
})();