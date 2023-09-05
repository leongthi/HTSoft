using CR_API.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Web.Http;

namespace CR_API.Controllers
{
    public class ClientsController : ApiController
    {
        [Route("api/clients/getall")]
        [HttpGet]
        public IEnumerable<Clients> GetAll()
        {
            using (QAOrgEntities dbContext = new QAOrgEntities())
            {
                return dbContext.Clients.ToList();
            }
        }
    }
}
