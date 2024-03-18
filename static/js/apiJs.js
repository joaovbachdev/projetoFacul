function salvaRelato(){
	content = document.getElementById("relatoInput").value
	$.ajax({
		url:'/salvaRelato',
		type:'POST',
		data:JSON.stringify({'content':content}),
		contentType:'application/json',
		sucess:function(response){
			console.log(response)
		},
		error:function(erro){
			console.log(error)
		}
	});
}
function validaLogin(nome, senha){
	$.ajax({
		url:'validaLogin',
		type:'POST',
		data:JSON.stringify({'usuario':nome, 'senha':senha}),
		contentType:'application/json',
		success:function(response){
			if(response=='valido'){
				window.location.href = "/"
			}
			//window.location.href = "/";
			console.log(response)
		},
		error:function(erro){
			console.log(erro)
		}
	});
}
function proximaPergunta(resposta,){
	texto = document.getElementById("pergunta")
	$.ajax({
		url:`/getPergunta?resposta=${resposta}`,
		type:'GET',
		success:function(response){
			if(response == 'PESQUISA FINALIZADA'){
				document.getElementById("btn-yes").style.display = 'none'
				document.getElementById("btn-no").style.display = 'none'
				document.getElementById("pergunta").classList.add("finalizada")
				document.getElementById('buttons').style.display = 'flex'

				document.getElementById('confetes').style.display = 'block'
			}else{
				texto.classList.add("animacao-texto")


			}
			texto.textContent = response
			setTimeout(() => {
				texto.classList.remove("animacao-texto")
		}, 1000);

			
			
		},
		error:function(error){
			console.log(error)
		}
	})
	
}

function salvaResultadoFinal(){
	professorNome = document.getElementById("professor").value
	$.ajax({
		url:'resultadoFinal',
		type:'POST',
		data:JSON.stringify({"professor":professorNome}),
		contentType: 'application/json',
		success:function(response){
			console.log(response)
			window.location.href = "/login"

		},
		error:function(erro){
			console.log(erro)
		}
	});
}

var timer = 0
function salvaAcao(acao, testes){
	$.ajax({
		url:'/salvaAcao',
		type:'POST',
		data:JSON.stringify({'acao':acao,'tempo':timer}),
		contentType:'application/json',
		success:function(response){
			timer = 0
			testesAutomaticos(testes)
		},
		error:function(error){
			console.log(error)
		}
	})
}

function atualizaTimer(){
	timer+=1
}
setInterval(atualizaTimer, 1000);