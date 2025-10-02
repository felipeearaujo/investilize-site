// @ts-check
import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';
import netlify from '@astrojs/netlify';

// https://astro.build/config
export default defineConfig({
  site: 'https://investilize.com.br',

  // ✅ CORREÇÃO FINAL: Usando a estrutura de objeto com 'entrypoint'
  image: {
    service: {
      entrypoint: 'astro/assets/services/sharp'
    }
  },

  integrations: [
    mdx(),
    sitemap()
  ],

  adapter: netlify({
  imageCDN: false
}),
});