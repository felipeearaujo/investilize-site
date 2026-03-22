// @ts-check
import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';
import netlify from '@astrojs/netlify';
import partytown from '@astrojs/partytown';

// https://astro.build/config
export default defineConfig({
  site: 'https://investilize.com.br',

  // ✅ CORREÇÃO FINAL: Usando a estrutura de objeto com 'entrypoint'
  image: {
    service: {
      entrypoint: 'astro/assets/services/sharp' // Nota: O padrão é 'sharp'. Se o seu estava 'grass' por erro, corrigi aqui.
    }
  },

  integrations: [mdx(), sitemap(), partytown()],

  // ✅ NOVO: Redirecionamento 301 para corrigir o erro de digitação da URL
  redirects: {
    // Redireciona a URL errada (sem a barra final) para a nova URL correta
    '/blog/renda-fix-veriavel-diferenca': { status: 301, destination: '/blog/renda-fixa-variavel-diferenca/' },
    // Redireciona a URL errada (com a barra final) para a nova URL correta
    '/blog/renda-fix-veriavel-diferenca/': { status: 301, destination: '/blog/renda-fixa-variavel-diferenca/' },
    
    // Opcional: Resolver a duplicação do Tesouro Direto se necessário
    // '/blog/tesouro-direto': { status: 301, destination: '/blog/tesouro-direto-guia/' },
  },

  adapter: netlify({
    imageCDN: false
  }),
});