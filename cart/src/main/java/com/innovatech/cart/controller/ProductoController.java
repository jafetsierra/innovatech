package com.innovatech.cart.controller;

import com.innovatech.cart.models.Producto;
import com.innovatech.cart.repo.ProductoRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@CrossOrigin
@RestController
@RequestMapping("/producto")
public class ProductoController {
    @Autowired
    private ProductoRepository productoRepository;

    //Obtener lista de productos
    @GetMapping("")
    List<Producto> index() {
        return productoRepository.findAll();
    }

    //Crear un nuevo producto
    @ResponseStatus(HttpStatus.CREATED)
    @PostMapping("")
    Producto create(@RequestBody Producto producto){
        return productoRepository.save(producto);
    }

    //Modificar un producto
    @PutMapping("{id}")
    Producto update(@PathVariable String id, @RequestBody Producto producto){
        Producto productoFromDB = productoRepository
                .findById(id)
                .orElseThrow(RuntimeException::new);
        productoFromDB.setName(producto.getName());
        productoFromDB.setPrice(producto.getPrice());
        productoFromDB.setDescription(producto.getDescription());
        productoFromDB.setCategory(producto.getCategory());
        productoFromDB.setStock(producto.getStock());

        return productoRepository.save(productoFromDB);
    }

    //Eliminar un producto
    @ResponseStatus(HttpStatus.NO_CONTENT)
    @DeleteMapping("{id}")
    void delete(@PathVariable String id){
        Producto producto = productoRepository
                .findById(id)
                .orElseThrow(RuntimeException::new);
        productoRepository.delete(producto);
    }
}
