function eliminarPelicula(id){
    Swal.fire({
        title: "Seguro de que desea eliminar esta pelicula?",
        showDenyButton:true,
        confirmButtonText:"Si",
        denyButtonText:"No"
    }).then((result)=>{
        if(result.isConfirmed){
            location.href = "/eliminarPelicula/" + id
        }
    })
}