// Ficheiro: src/pages/api/cotacao.ts
import type { APIRoute } from 'astro';

// A LINHA MÁGICA QUE RESOLVE TUDO!
// Diz ao Astro para tratar este ficheiro como um endpoint dinâmico de servidor.
export const prerender = false;

export const POST: APIRoute = async ({ request }) => {
  const apiKey = import.meta.env.ALPHA_VANTAGE_API_KEY;

  if (!apiKey) {
    return new Response(JSON.stringify({ error: 'A chave da API não foi configurada no servidor.' }), { status: 500 });
  }

  try {
    const body = await request.json();
    const symbol = body.symbol;

    if (!symbol) {
      return new Response(JSON.stringify({ error: 'O símbolo da ação é obrigatório no corpo do pedido.' }), { status: 400 });
    }

    const externalApiUrl = `https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=${symbol}&apikey=${apiKey}`;
    const externalResponse = await fetch(externalApiUrl);
    
    if (!externalResponse.ok) {
        throw new Error("Falha na comunicação com a API externa de cotações.");
    }

    const data = await externalResponse.json();
    
    if (data["Error Message"] || !data["Global Quote"] || Object.keys(data["Global Quote"]).length === 0) {
       return new Response(JSON.stringify({ error: 'Não foi possível obter a cotação. Verifique o símbolo ou a sua chave de API.' }), { status: 404 });
    }

    return new Response(JSON.stringify(data["Global Quote"]), {
      status: 200,
      headers: { 'Content-Type': 'application/json' }
    });

  } catch (error) {
    let message = 'Erro ao processar o pedido.';
    if(error instanceof Error) message = error.message;
    return new Response(JSON.stringify({ error: message }), { status: 400 });
  }
};