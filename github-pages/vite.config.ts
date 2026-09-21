import {defineConfig} from 'vite';
import react from '@vitejs/plugin-react';
import {fileURLToPath} from 'node:url';
const root=fileURLToPath(new URL('..',import.meta.url));
export default defineConfig({
 root:root+'github-pages',
 base:'./',
 publicDir:root+'public',
 plugins:[react()],
 resolve:{alias:{'@':root}},
 css:{postcss:root},
 build:{outDir:root+'docs',emptyOutDir:true,sourcemap:false},
 server:{host:'0.0.0.0',port:4181,strictPort:true,allowedHosts:['terminal.local']},
});
