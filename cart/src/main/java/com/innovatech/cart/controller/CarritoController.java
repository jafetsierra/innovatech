package com.innovatech.cart.controller;

import com.innovatech.cart.models.Carrito;
import com.innovatech.cart.repo.CarritoRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@CrossOrigin
@RestController
@RequestMapping("/carrito")
public class CarritoController {
    @Autowired
    private CarritoRepository carritoRepository;

    //Obtener lista con los productos en el carrito
    @GetMapping("{userId}")
    List<Carrito> index(@PathVariable String userId) {
        return carritoRepository.findByUserId(userId);
    }

    //Añadir producto al carrito
    @ResponseStatus(HttpStatus.CREATED)
    @PostMapping("")
    Carrito create(@RequestBody Carrito carrito){
        return carritoRepository.save(carrito);
    }

    //Modificar la cantidad de un producto del carrito
    @PutMapping("")
    Carrito update(@RequestBody Carrito carrito){
        Carrito carritofromDB = carritoRepository
                .findByProductIdAndUserId(carrito.getProductId(), carrito.getUserId());
        carritofromDB.setAmount(carrito.getAmount());

        return carritoRepository.save(carritofromDB);
    }

    //Eliminar producto del carrito dado el id del producto
    @ResponseStatus(HttpStatus.ACCEPTED)
    @DeleteMapping("{userId}")
    void delete(@PathVariable String userId, @RequestBody Carrito carrito){
        Carrito carritofromDB = carritoRepository
                .findByProductIdAndUserId(carrito.getProductId(),userId);
        carritoRepository.delete(carritofromDB);
    }
}
