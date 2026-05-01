import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

// 1. Coleção Blog (Aponta especificamente para a pasta content/blog)
const blog = defineCollection({
    loader: glob({ pattern: '**/[^_]*.{md,mdx}', base: "./src/content/blog" }),
    schema: z.object({
        title: z.string(),
        description: z.string(),
        pubDate: z.coerce.date(),
        author: z.string().optional(),
        heroImage: z.string().optional(),
        faqList: z.array(
            z.object({
                question: z.string(),
                answer: z.string(),
            })
        ).optional(),
    }),
});

// 2. Coleção Notícias (Aponta especificamente para a pasta content/noticias)
const noticias = defineCollection({
    loader: glob({ pattern: '**/[^_]*.{md,mdx}', base: "./src/content/noticias" }),
    schema: z.object({
        title: z.string(),
        description: z.string(),
        pubDate: z.coerce.date(),
        originalUrl: z.string(),
    }),
});

// 3. Exporta todas as coleções de forma limpa
export const collections = { blog, noticias };import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

// 1. Coleção Blog (Aponta especificamente para a pasta content/blog)
const blog = defineCollection({
    loader: glob({ pattern: '**/[^_]*.{md,mdx}', base: "./src/content/blog" }),
    schema: z.object({
        title: z.string(),
        description: z.string(),
        pubDate: z.coerce.date(),
        author: z.string().optional(),
        heroImage: z.string().optional(),
        faqList: z.array(
            z.object({
                question: z.string(),
                answer: z.string(),
            })
        ).optional(),
    }),
});

// 2. Coleção Notícias (Aponta especificamente para a pasta content/noticias)
const noticias = defineCollection({
    loader: glob({ pattern: '**/[^_]*.{md,mdx}', base: "./src/content/noticias" }),
    schema: z.object({
        title: z.string(),
        description: z.string(),
        pubDate: z.coerce.date(),
        originalUrl: z.string(),
    }),
});

// 3. Exporta todas as coleções de forma limpa
export const collections = { blog, noticias };
