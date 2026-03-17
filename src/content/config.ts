import { defineCollection, z } from 'astro:content';

const noticias = defineCollection({
	type: 'content',
	schema: z.object({
		title: z.string(),
		description: z.string(),
		// Transforma a string de data em um objeto Date do JS
		pubDate: z.coerce.date(),
		originalUrl: z.string(),
	}),
});

// Exporta as coleções (adiciona 'noticias' à lista)
export const collections = { 
    'blog': defineCollection({ /* sua config de blog atual */ }),
    'noticias': noticias 
};