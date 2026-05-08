// @ts-check
import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';
import netlify from '@astrojs/netlify';
import partytown from '@astrojs/partytown';

// Importe as dependências de matemática aqui:
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';

// https://astro.build/config
export default defineConfig({
  site: 'https://investilize.com.br',
  
  markdown: {
    remarkPlugins: [remarkMath],
    rehypePlugins: [
      // ✅ O plugin e as opções DEVEM estar dentro de um array próprio
      [rehypeKatex, {
        strict: false,
        throwOnError: false
      }]
    ],
  },

  // ✅ Mantém a barra final em todos os links para alinhar com a Netlify
  trailingSlash: 'always',

  build: {
    format: 'directory' // Cria pastas físicas (index.html) para cada post, excelente para SEO
  },

  image: {
    service: {
      entrypoint: 'astro/assets/services/sharp'
    }
  },

  integrations: [
    mdx(), // Permite usar componentes dentro do seu conteúdo
    sitemap(), 
    partytown()
  ],

  // ✅ CORREÇÃO: Apenas uma rota de redirecionamento para evitar colisão
  redirects: {
    '/blog/renda-fix-veriavel-diferenca/': { status: 301, destination: '/blog/renda-fixa-variavel-diferenca/' },
  },

  adapter: netlify({
    imageCDN: false
  }),
});