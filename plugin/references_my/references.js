/* Scans the reference tags, and numbers them in the order of appearance */
'use strict';

(() => {

   const ref_order = new Map();

   // Find all references in the document (returned in order of their
   // appearance)
   const references = document.getElementsByClassName("ref");

   
   // If there are no references, just return immediately.
   if (references.length == 0) {
      return;
   }

   // Otherwise, run over the elements, and add the corresponding numbering
   // to the tags.
   let ref_counter = 0;
   for (let i = 0; i < references.length; i++) {
      let ref_id = references[i].id;
      // If the reference has already been seen, just use its original
      // numbering
      let ref_num = -1;
      if (ref_order.has(ref_id)) {
         ref_num = ref_order.get(ref_id);
      } else {
         ref_counter += 1;
         ref_num = ref_counter;
         console.log(ref_id)
         console.log(ref_counter)
         console.log("-------")
         ref_order.set(ref_id, ref_counter)
      }
      references[i].innerText = `[${ref_num}]`
   }
})()
